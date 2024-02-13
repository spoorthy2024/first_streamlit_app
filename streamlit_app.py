import streamlit
import pandas
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & Blueberry Oat meal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔Hard Boiled free range egg')
streamlit.text('🥑🍞Avacodo toast')
streamlit.header('🍌🥭Build your own fruit smoothie🥝🍇')
my_fruits_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put the list here,so they can pick whatever fruit they want
streamlit.multiselect("pick some fruits:",list(my_fruits_list.index))
streamlit.dataframe(my_fruits_list);
