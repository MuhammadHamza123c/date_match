if name:
    # Ensure that the name exists in the data before trying to access its index
    if name in data['Name'].values:
        user_name = data[data['Name'] == name].index[0]
        
        # Calculate cosine similarity
        similarities = similar[user_name]

        # Sort and get the top 2 recommended matches
        indexed_arr = list(enumerate(similarities))
        sorted_indexed_arr = sorted(indexed_arr, key=lambda x: x[1], reverse=True)

        # Exclude the user's own index and gender
        top_2_indices = []
        for index, _ in sorted_indexed_arr:
            if data['Name'].iloc[index] != name and data['Gender'].iloc[index] != data['Gender'].iloc[user_name]:
                top_2_indices.append(index)
            if len(top_2_indices) == 2:  # Limit to top 2 matches
                break

        # Display user and match details
        st.markdown("##### IT WILL TAKE US FEW SECONDS TO FIND YOUR MATCH MAKER😉.......")
        t.sleep(3)

        # Display the user's profile
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

        # Display matches
        for i in top_2_indices:
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
    else:
        st.error("Name not found in the dataset.")
