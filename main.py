import streamlit as st
st.image('./header.png', caption='Making History', use_column_width=True)
st.title("1RM Calculator")

weight = st.number_input("Enter your Weight", min_value=0, step=1, value=0)
reps = st.number_input("Enter your Reps", min_value=0, step=1, value=0)

if st.button("Calculate 1RM"):
    results = weight / (1.0278 - 0.0278 * reps)
    st.write(f"Your 1RM is: {results:.2f}")

st.title("Kg to Lbs")
Kg = st.number_input("Enter Weight in Kg", min_value=0, step=1, value=0)

if st.button("Convert Kg"):
    results = Kg * 2.2
    st.write(f"lbs: {results:.2f}")

st.title("Lbs to Kg")
Lbs = st.number_input("Enter Weight in Lbs", min_value=0, step=1, value=0)

if st.button("Convert Lbs"):
    results = Lbs / 2.2
    st.write(f"lbs: {results:.2f}")
