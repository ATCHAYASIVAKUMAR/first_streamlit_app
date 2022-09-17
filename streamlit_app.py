import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header(' Breakfast Favourites')

streamlit.text('😜😜chicken briyani and lollipop')
streamlit.text('kalaki egg')

streamlit.header('Lunch Favourites of the day')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacado','Strawberries'])

