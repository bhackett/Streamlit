# https://medium.com/pythoneers/forget-html-and-flask-start-using-streamlit-1b394cfe4595
# http://localhost:8501/ for results

# import modules
import pandas as pd
import streamlit as st

# Title
st.title("This is Title line")

# Header
st.header("This is a header")

# Subheader
st.subheader("This line belongs to a subheader")

# Text
st.text("This line belongs to a text")

# Markdowns
st.markdown("### This is a markdown")
st.markdown("## This is a markdown")
st.markdown("# This is a markdown")

# Reading the CSV file
df = pd.read_csv("Startups_Expense.csv")
# Putting title
st.title("View of the Data shown below:")
# To visualize the data
st.write(df)

# Title and option of radio button
status = st.radio("Select Subject: ", ('English', 'Math'))
# Choice based on condition
if status == 'English':
    st.success("English")
else:
    st.success("Math")

# slider
house_number = st.slider("Select the number", 1, 5)
# Fetching and Printing the house number
st.text('Selected House Number: {}'.format(house_number))

# slider
house_number = st.slider('house_number', min_value=1, max_value=10, step=1)
# Fetching and Printing the house number
st.text('Selected House Number: {}'.format(house_number))

# Select the subject from the Selectbox
subject = st.selectbox("Subjects: ",['English', 'Hindi', 'Math', 'Science'])
# Print the subject
st.write("Your Subject is: ", subject)

# Select the subject from the Multi Select option
subject = st.multiselect("Subjects: ",['English', 'Hindi', 'Math', 'Science'])
# Print the subject
st.write("Your Subject is: ", len(subject), 'subject')
