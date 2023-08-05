# Author: Nicholas Eby
# Date Created: August 5, 2023
import streamlit as st

st.markdown(
    """ # Welcome to Content Generator!
        Fill out the inputs to create AI content.
    """
)

prompt = ""

content_type = st.selectbox("Select Content Type", ["Tweet", "Caption", "One Page Article"])
subject = st.text_input("Enter Subject")

# length = st.selectbox("Select Length", [])

    
if content_type and subject:
    prompt += "Write a " + content_type + " about " + subject

if content_type == "Tweet":
    pass
elif content_type == "Caption":
    pass
elif content_type == "Article":
    pass

# slider_num = st.slider('Pick a number:', 1, 10000)

submit = st.button("Submit")
if submit:
    st.title(prompt)
    print(prompt)

        