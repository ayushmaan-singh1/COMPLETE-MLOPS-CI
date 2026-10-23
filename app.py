import streamlit as st
st.title("Power Calculator")
st.write("Enter a number to calculate Suare, Cube and Fifth Power.")


# Get user input
n = st.number_input("Enter an integer", value=1, step=1)


#Calculate result
sqr = n ** 2
cube = n ** 3
fifth = n ** 5

#Display results
st.write(f"Square of {n} is: {sqr}")
st.write(f"Cube of {n} is: {cube}")
st.write(f"Fifth of {n} is: {fifth}")