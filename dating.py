import pandas as pd
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import time as t

col1, col2 = st.columns(2)
vector = TfidfVectorizer()

st.markdown("# MATCH MAKER 🤝💕")

# Initialize session state
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Load existing data
data = pd.read_csv("match.csv")
st.info("Make sure to fill out all the information in sequence.")

# Collect user input
with st.form("user_form"):
    st.markdown("###### Write down Name here: ")
    name = st.text_input("", key="name_input")

    st.markdown("###### Write down age here: ")
    age = st.number_input("", key="age_input", format="%d", step=1)

    st.markdown("###### Write down gender here: ")
    gender = st.radio("", ['Male', 'Female'], index=0, key="gender_radio")

    st.markdown("###### Write down hobbies here: ")
    hobbies = st.text_input("", key="hobbies_input")

    st.markdown("###### How would you describe your communication style?")
    comm = st.radio('', ['Direct and to the point', 'Friendly and chatty', 
                        'Calm and thoughtful', 'Depends on the situation'], index=0, key="comm_radio")

    st.markdown("###### Write down Your Favorite Subject here: ")
    fav_subject = st.text_input("", key="fav_sub_input")

    st.markdown("###### Write down Your Favorite Singer here: ")
    fav_singer = st.text_input("", key="fav_singer_input")

    st.markdown("###### Write down Grade here: ")
    grade = st.radio("", ['A', 'B', 'C', 'D', 'F'], index=0, key="grade_radio")

    submitted = st.form_submit_button("Find Matches!")

if submitted:
    st.session_state.submitted = True
    # Create new entry
    new_entry = pd.DataFrame([{
        'Name': name,
        'Age': age,
        'Gender': gender,
        'Hobbies': hobbies,
        'Communication': comm,
        'Fav_sub': fav_subject,
        'Fav_singer': fav_singer,
        'Grade': grade
    }])

    # Update dataset
    data = pd.concat([data, new_entry], ignore_index=True)
    data.to_csv("match.csv", index=False)

    # Prepare data for similarity
    combined_features = (
        data['Age'].astype(str) + ' ' +
        data['Gender'] + ' ' +
        data['Hobbies'] + ' ' +
        data['Communication'] + ' ' +
        data['Fav_singer'] + ' ' +
        data['Fav_sub'] + ' ' +
        data['Grade']
    )

    # Calculate similarity
    tfidf_matrix = vector.fit_transform(combined_features)
    cosine_sim = cosine_similarity(tfidf_matrix)
    
    # Get current user index
    user_index = data[data['Name'] == name].index[0]
    
    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[user_index]))
    
    # Filter out user and same gender
    opposite_gender = 'Female' if gender == 'Male' else 'Male'
    filtered_scores = [
        (i, score) for i, score in sim_scores 
        if i != user_index and data.iloc[i]['Gender'] == opposite_gender
    ]
    
    # Sort by score
    filtered_scores = sorted(filtered_scores, key=lambda x: x[1], reverse=True)
    
    # Get top 2 matches
    top_indices = [i for i, _ in filtered_scores[:2]]

    # Display results
    st.markdown("##### IT WILL TAKE US FEW SECONDS TO FIND YOUR MATCH MAKER😉.......")
    t.sleep(3)
    
    with col1:
        st.markdown("#### You!!")
        st.write(f"Name: {name}")
        st.write(f"Age: {age}")
        st.write(f"Gender: {gender}")
        st.write(f"Hobbies: {hobbies}")
        st.write(f"Communication: {comm}")
        st.write(f"Favorite Subject: {fav_subject}")
        st.write(f"Favorite Singer: {fav_singer}")
        st.write(f"Grade: {grade}")

    with col2:
        if top_indices:
            st.markdown("#### Top Matches")
            for idx in top_indices:
                match = data.iloc[idx]
                st.write("---")
                st.write(f"Name: {match['Name']}")
                st.write(f"Age: {match['Age']}")
                st.write(f"Gender: {match['Gender']}")
                st.write(f"Hobbies: {match['Hobbies']}")
                st.write(f"Communication: {match['Communication']}")
                st.write(f"Favorite Subject: {match['Fav_sub']}")
                st.write(f"Favorite Singer: {match['Fav_singer']}")
                st.write(f"Grade: {match['Grade']}")
        else:
            st.warning("No suitable matches found!")

    st.markdown("##### SCROLL UP")
