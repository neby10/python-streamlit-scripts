# Author: Nicholas Eby
# Date Created: August 5, 2023

import streamlit as st
import google.generativeai as palm
import os
from dotenv import load_dotenv
load_dotenv()

PALM_KEY = os.getenv('PALM_KEY')
palm.configure(api_key=PALM_KEY)

defaults = {
    'model': 'models/chat-bison-001',
    'temperature': 0.25,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
}

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

DEFAULT_VALUE = "No Preference"

CUISINE_TYPES = [DEFAULT_VALUE, "American", "Chinese", "Italian", "Mexican", "French", "Japanese", "Mediterranean", "Thai", "Indian", "Greek"]
MOVIE_GENRES = [DEFAULT_VALUE, "Action", "Comedy", "Romance", "SciFi", "Thriller", "Horror", "Documentary", "Animation", "Mystery", "Crime"]
BOOK_GENRES = [DEFAULT_VALUE, "Fiction", "Science Fiction", "Historical Fiction", "Fantasy", "Non-fiction", "Mystery", "Self-Help", "Biography", "Romance"]

MATURITY_RATINGS = [DEFAULT_VALUE, "G", "PG", "PG-13", "R", "Not Rated"]
READING_LEVELS = [DEFAULT_VALUE, "Child", "Elementary", "Middle School", "High School", "Adult"]

LENGTHS = [DEFAULT_VALUE, "Short", "Medium", "Long"]

question = st.selectbox("Select a Question to Ask", [QUESTION1, QUESTION2, QUESTION3])

if question == QUESTION1: # Dinner => location, price, cuisine
    prompt += QUESTION1 + " Use this information to help give suggestions: "
    location = st.text_input("Location")
    num_people = st.slider("Number of People", 1, 10)
    price = st.text_input("Approximate Total Price (USD)")
    cuisine = st.selectbox("Cuisine", CUISINE_TYPES)
    if location:
        prompt += "Location: " + location + ", "
    if num_people:
        prompt += "Number of People: " + str(num_people) + ", "
    if price:
        prompt += "Price: $" + price + ", "
    if cuisine:
        prompt += "Cuisine: " + cuisine + ", "
elif question == QUESTION2: # Movie => Genre, Length, Maturity
    prompt += QUESTION2 + " Use this information to help give suggestions: "
    genre = st.selectbox("Genre", MOVIE_GENRES)
    length = st.selectbox("Length of movie: ", LENGTHS)
    maturity = st.selectbox("Movie Rating: ", MATURITY_RATINGS)
    if genre:
        prompt += "Genre: " + genre + ", "
    if length:
        prompt += "Movie Length: " + length + ", "
    if maturity:
        prompt += "Maturity Rating: " + maturity + ", "
elif question == QUESTION3: # Book => Genre, Length, Reading Level
    prompt += QUESTION3 + " Use this information to help give suggestions: "
    genre = st.selectbox("Genre", BOOK_GENRES)
    length = st.selectbox("Length of book: ", LENGTHS)
    reading_level = st.selectbox("Reading Level: ", READING_LEVELS)
    if genre:
        prompt += "Genre: " + genre + ", "
    if length:
        prompt += "Book Length: " + length + ", "
    if reading_level:
        prompt += "Reading Level: " + reading_level + ", "
else:
    print("Error")

limit_options = st.slider("Limit options:", 1, 20)
if limit_options:
    prompt += "Limit number of options to " + str(limit_options)

submit = st.button("Submit")
if submit:
    print("Prompt: ", prompt)
    response = palm.chat(**defaults, messages=prompt)
    st.write(response.last)
    print(response.last)