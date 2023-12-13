import streamlit as st
import requests

response = requests.get('https://api.nasa.gov/planetary/apod?api_key='
                        '{ENTER YOUR API KEY}')

data = response.json()

# get the image and create an image file to display it
image = requests.get(data['hdurl'])
with open('today_image.jpg', 'wb') as file:
    file.write(image.content)

# display the title
st.title(data['title'])

# display the image
st.image('today_image.jpg')

# display the explanation
st.write(data['explanation'])
