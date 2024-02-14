import streamlit
import pandas
import requests
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & Blueberry Oat meal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔Hard Boiled free range egg')
streamlit.text('🥑🍞Avacodo toast')
streamlit.header('🍌🥭Build your own fruit smoothie🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
# New Section to display fruitvicey response
streamlit.header('Fruity vice fruit advice')
fruitvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# take json version of response and normalize it
fruityvice_normalized = pandas.json_normalize(fruitvice_response.json())
streamlit.dataframe(fruityvice_normalized);

