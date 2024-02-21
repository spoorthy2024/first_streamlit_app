import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
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
streamlit.header('FruityVice fruit advice')
try:
  fruit_choice = streamlit.text_input('what fruit information would you like ?')
  if not fruit_choice:
    streamlit.error("please enter the fruit to get information")
  else:
    fruitvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    # take json version of response and normalize it
    fruityvice_normalized = pandas.json_normalize(fruitvice_response.json())
    streamlit.dataframe(fruityvice_normalized);
except URLError as e:
  streamlit.error()
# don't run anything here while we trouble shoot
streamlit.stop();
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("some fruits from fruits_list")
streamlit.dataframe(my_data_row)
fruit_add = streamlit.text_input('what fruit would you like to add')
streamlit.text("Thanks for adding " + fruit_add)
#my_cur.execute("insert into fruit_load_list values('from streamlite')")




