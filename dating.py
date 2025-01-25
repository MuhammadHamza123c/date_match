import pandas as pd
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import time as t
col1,col2=st.columns(2)


vector = TfidfVectorizer()

st.markdown("# MATCH MAKER 🤝💕")

Name = []
Age = []
Gender=[]
Hobbies=[]
Communication = []
Fav_sub = []
Fav_singer = []
Grade = []


data = pd.read_csv("match.csv")
st.info("Make sure to fill out all the information in sequence.")

st.markdown("###### Write down Name here: ")
    # Create a unique key by including the field name
name = st.text_input("", key=f"name_input_{len(Name)}")
if name:
      Name.append(name)

st.markdown("###### Write down age here: ")
age = st.number_input("", key=f"age_input_{len(Age)}",format="%d",step=1)
if age:
     
     Age.append(age)

st.markdown("###### Write down gender here: ")

gender=st.radio(
   "",
   ['Select Gender','Male','Female'],
   index=0
)
if gender!='Select Gender':
   Gender.append(gender)

st.markdown("###### Write down hobbies here: ")

hobbies=st.text_input("")
if hobbies:
        Hobbies.append(hobbies)

st.markdown("###### How would you describe your communication style?")   
comm = st.radio(
   '',
   ['Select Communication Style','Direct and to the point','Friendly and chatty','Calm and thoughtful','Depends on the situation'],
   index=0
)
if comm!='Select Communication Style':

 Communication.append(comm)

st.markdown("###### Write down Your Favorite Subject here: ")
    
Fav_subject = st.text_input("", key=f"fav_sub_input_{len(Fav_sub)}")

if Fav_subject:
        Fav_sub.append(Fav_subject)
st.markdown("###### Write down Your Favorite Singer here:  ")
    
Fav_singerr = st.text_input("", key=f"fav_singer_input_{len(Fav_singer)}")

if Fav_singerr:
     
       Fav_singer.append(Fav_singerr)
st.markdown("###### Write down Grade here: ")
    
grade = st.radio(
   "",
   ['Select Grade','A','B','C','D','F'],
   index=0
)
if grade!='Select Grade':
        Grade.append(grade)
    
        # Add the new data to the DataFrame
        dataset = pd.DataFrame({
            'Name': Name,
            'Age': Age,
            'Gender':Gender,
            'Hobbies':Hobbies,
            'Communication': Communication,
            'Fav_sub': Fav_sub,
            'Fav_singer': Fav_singer,
            'Grade': Grade
        })
    
        data = pd.concat([data, dataset], ignore_index=True)
    
        # Save the updated data to the CSV file
        data.to_csv("match.csv", index=False)
    
        # Create a string combining all the features for similarity calculation
        changing = data['Age'].astype(str) + '' +data['Gender'].astype(str)+ '' +data['Hobbies']+ '' +data['Communication'].astype(str) + '' + data['Fav_singer'].astype(str) + '' + data['Fav_sub'].astype(str) + '' + data['Grade'].astype(str)
        change_data = vector.fit_transform(changing)
        matrix = change_data.toarray()
    
        # Calculate cosine similarity
        similar = cosine_similarity(matrix)
        user_name = data[data['Name'] == name].index[0]
        similarities = similar[user_name]
    
        # Sort and get the top 2 recommended matches
        indexed_arr = list(enumerate(similarities))
        sorted_indexed_arr = sorted(indexed_arr, key=lambda x: x[1], reverse=True)
        top_2_indices = [index for index, value in sorted_indexed_arr[:2]]
        st.markdown("##### IT WILL TAKE US FEW SECONDS TO FIND YOUR MATCH MAKER😉.......")
        t.sleep(3)
        with col1:
               st.markdown("#### You!!")
               st.write(f"Name: {data['Name'].iloc[user_name]}")
               st.write(f"Age: {data['Age'].iloc[user_name]}")
               st.write(f"Gender: {data['Gender'].iloc[user_name]}")
               st.write(f"Hobbies: {data['Hobbies'].iloc[user_name]}")
               st.write(f"Communication: {data['Communication'].iloc[user_name]}")
               st.write(f"Favorite Subject: {data['Fav_sub'].iloc[user_name]}")
               st.write(f"Favorite Singer: {data['Fav_singer'].iloc[user_name]}")
               st.write(f"Grade: {data['Grade'].iloc[user_name]}")
        
              

    
        
        for i in top_2_indices:
            
            if data['Name'].iloc[i]==name and data['Gender'].iloc[i]==data['Gender'].iloc[i]:
                  continue
            with col2:
             st.markdown("#### Meet Your Match!!")
             st.write(f"Name: {data['Name'].iloc[i]}")
             st.write(f"Age: {data['Age'].iloc[i]}")
             st.write(f"Gender: {data['Gender'].iloc[i]}")
             st.write(f"Hobbies: {data['Hobbies'].iloc[i]}")
             st.write(f"Communication: {data['Communication'].iloc[i]}")
             st.write(f"Favorite Subject: {data['Fav_sub'].iloc[i]}")
             st.write(f"Favorite Singer: {data['Fav_singer'].iloc[i]}")
             st.write(f"Grade: {data['Grade'].iloc[i]}")
             t.sleep(2)
        st.markdown("##### SCROLL UP")     
