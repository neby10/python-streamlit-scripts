# Author: Nicholas Eby
# Date Created: August 5, 2023

import streamlit as st

st.markdown(
    """ # Welcome to Answer Questions!
        Fill out the inputs to answer a question.
    """
)

prompt = ""

# DEFINE CONSTANTS
QUESTION1 = "What should we eat for dinner?"
QUESTION2 = "What movie should we watch?"
QUESTION3 = "What book should I read next?"

CUISINE_TYPES = ["American", "Chinese", "Italian", "Mexican", "French", "Japanese", "Mediterranean", "Thai", "Indian", "Greek"]
MOVIE_GENRES = ["Action", "Comedy", "Romance", "SciFi", "Horror", "Thriller", "Horror", "Documentary", "Animation", "Mystery", "Crime"]
BOOK_GENRES = ["Fiction", "Science Fiction", "Historical Fiction", "Fantasy", "Non-fiction", "Mystery", "Self-Help", "Biography", "Romance"]

MATURITY_RATINGS = ["G", "PG", "PG-13", "R", "Not Rated"]
READING_LEVELS = ["Child", "Elementary", "Middle School", "High School", "Adult"]

question = st.selectbox("Select a Question to Ask", [QUESTION1, QUESTION2, QUESTION3])

if question == QUESTION1: # Dinner => location, price, cuisine
    prompt += QUESTION1 + " Use this information to help give suggestions: "
    location = st.text_input("Location")
    price = st.text_input("Approximate Total Price")
    cuisine = st.selectbox("Cuisine", CUISINE_TYPES)
    if location:
        prompt += "Location: " + location + ", "
    if price:
        prompt += "Price: " + price + ", "
    if cuisine:
        prompt += "Cuisine: " + cuisine + ", "
elif question == QUESTION2: # Movie => Genre, Length, Maturity
    prompt += QUESTION2 + " Use this information to help give suggestions: "
    genre = st.selectbox("Genre", MOVIE_GENRES)
    length = st.slider("Length of movie in minutes: ", 45, 210)
    maturity = st.selectbox("Movie Rating: ", MATURITY_RATINGS)
    if genre:
        prompt += "Genre: " + genre + ", "
    if length:
        prompt += "Length (in munutes): " + str(length) + ", "
    if maturity:
        prompt += "Maturity Rating: " + maturity + ", "
elif question == QUESTION3: # Book => Genre, Length, Reading Level
    prompt += QUESTION3 + " Use this information to help give suggestions: "
    genre = st.selectbox("Genre", BOOK_GENRES)
    length = st.slider("Length of book in pages: ", 25, 1000)
    reading_level = st.selectbox("Reading Level: ", READING_LEVELS)
    if genre:
        prompt += "Genre: " + genre + ", "
    if length:
        prompt += "Length (in pages): " + str(length) + ", "
    if reading_level:
        prompt += "Reading Level: " + reading_level + ", "
else:
    print("Error")

submit = st.button("Submit")
if submit:
    print("Prompt: ", prompt)