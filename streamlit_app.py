import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title(' wohooo !!! My first Streamlit Program')

streamlit.header('Menu')
streamlit.text('🐔 Chicken curry')
streamlit.text('🥣 Paneer curry')
streamlit.text('🍞 Chapati')

streamlit.title('Build your own smoothie')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

#New section to display Fruityvice api response

streamlit.header('Fruityvice fruit advice!!')

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

#normalize json data
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like information about?','banana')
streamlit.write('The user entered ', add_my_fruit)

my_cur.execute("insert into fruit_load_list values('from streamlit')")







