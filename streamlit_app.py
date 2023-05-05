import streamlit


streamlit.title(' wohooo !!! My first Streamlit Program')

streamlit.header('Menu')
streamlit.text('🐔 Chicken curry')
streamlit.text('🥣 Paneer curry')
streamlit.text('🍞 Chapati')

streamlit.title('Build your own smoothie')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

#New section to display Fruityvice api response
import requests
streamlit.header('Fruityvice fruit advice!!')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
