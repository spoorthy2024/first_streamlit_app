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
# create a repeatable code block called function
def get_fruityvice_data(this_fruit_choice):
  fruitvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  # take json version of response and normalize it
  fruityvice_normalized = pandas.json_normalize(fruitvice_response.json())
  return fruityvice_normalized
  
# New Section to display fruitvicey response
streamlit.header('FruityVice fruit advice')
try:
  fruit_choice = streamlit.text_input('what fruit information would you like ?')
  if not fruit_choice:
    streamlit.error("please enter the fruit to get information")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()
streamlit.header("View our Fruit List - Add your Favourites")
# snow-flake related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * FROM pc_rivery_db.public.fruit_load_list")
    return my_cur.fetchall()
# Add the button to load fruit_list
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)
# Allow end user to add fruit to the list
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("INSERT INTO fruit_load_list VALUES (%s)", (new_fruit,))
    return "Thanks for adding " + new_fruit
fruit_add = streamlit.text_input('what fruit would you like to add')
if streamlit.button('Add fruit to list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(fruit_add)
  streamlit.text(back_from_function)
  
  
  




