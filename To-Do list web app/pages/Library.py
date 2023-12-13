from PIL import Image
import streamlit as st
import os

# camera widget with download button
with st.expander(label='Camera'):
    photo = st.camera_input(label='')
    if photo:
        st.download_button('Download Photo', photo, 'photo.jpg')

# upload new photos from the user
uploaded_images = st.file_uploader('Upload Image', accept_multiple_files=True)
for uploaded_image in uploaded_images:
    img = Image.open(uploaded_image)
    img.save(f'Photos/{uploaded_image.name}')

# get all the photos names
photos = os.listdir('Photos')


def delete_photo(photo):
    """ delete photos if delete button is pressed """
    os.remove(f'Photos/{photo}')


col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])

if photos:
    # show all the photos in the library
    with col1:
        for photo in photos[::2]:
            img = Image.open(f'Photos/{photo}')
            st.image(img)
            st.button('Delete', on_click=delete_photo, args=(photo,), key=photo)

    with col2:
        for photo in photos[1::2]:
            img = Image.open(f'Photos/{photo}')
            st.image(img)
            st.button('Delete', on_click=delete_photo, args=(photo,), key=photo)
