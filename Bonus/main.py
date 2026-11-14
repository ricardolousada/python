import streamlit as st
from PIL import Image

with st.expander("Start camera"):
    #strat the camera
    photo = st.camera_input("Camara")

if photo:
    st.image(photo)
    #create a pillow image instance
    img= Image.open(photo)
    # covert the pillow image to gray scale
    gray_img = img.convert('L')
    #render the image in grayscale
    st.image(gray_img)



