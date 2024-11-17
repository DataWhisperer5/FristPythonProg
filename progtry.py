import streamlit as st
from PIL import Image

# Display the title of the app
st.title("Picture and Buttons App")

# Resize the image dynamically
img_path = "manja-vitolic-gKXKBY-C-Dk-unsplash.jpg"  # Upload the file to your GitHub repository
img = Image.open(img_path)
img = img.resize((300, 200))  # Adjust the dimensions as needed

# Display the image
st.image(img, caption="This is the resized image", use_column_width=False)

# Define actions for buttons
if st.button("Button 1"):
    st.write("Button 1 clicked!")

if st.button("Button 2"):
    st.write("Button 2 clicked!")

if st.button("Button 3"):
    st.write("Button 3 clicked!")
