import streamlit as st

st.title("1RM Calculator")

st.write("Enter your Weight:")
weight = st.number_input("", value=0, step=1)

st.write("Enter your Reps:")
reps = st.number_input("", value=0, step=1)

if st.button("Calculate 1RM"):
    results = weight / (1.0278 - 0.0278 * reps)
    st.write(f"Your 1RM is: {results:.2f}")

# 1RM = weight / ( 1.0278 – 0.0278 × reps )
