#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# Define a function to calculate BMI
def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return bmi

# Define the Streamlit app
def app():
    # Set the page title
    st.set_page_config(page_title="BMI Calculator", page_icon=":hospital:")

    # Add the controls to the app
    st.write("# BMI Calculator")
    name = st.text_input("Name")
    gender = st.radio("Gender", options=["Male", "Female", "Other"])
    age = st.number_input("Age", min_value=1, max_value=120, value=18)
    address = st.text_area("Address")
    hobbies = st.multiselect("Hobbies", options=["Reading", "Sports", "Music", "Traveling"])
    weight = st.number_input("Weight (kg)", min_value=1, max_value=500, value=60)
    height = st.number_input("Height (cm)", min_value=1, max_value=300, value=170)

    # Calculate BMI based on the user's input
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI is {bmi:.2f}")

if __name__ == "__main__":
    app()

