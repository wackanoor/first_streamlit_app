import streamlit


streamlit.title(' wohooo !!! My first Streamlit Program')

streamlit.header('Menu')
streamlit.text('🐔 Chicken curry')
streamlit.text('🥣 Paneer curry')
streamlit.text('🍞 Chapati')

streamlit.title('Build your own smoothie')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


