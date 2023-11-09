import streamlit as st
st.image('./header.png', caption='Making History', use_column_width=True)
st.title("1RM Calculator")

weight = st.number_input("Enter your Weight", min_value=0, step=1, value=0)
reps = st.number_input("Enter your Reps", min_value=0, step=1, value=0)

if st.button("Calculate 1RM"):
    results = weight / (1.0278 - 0.0278 * reps)
    st.write(f"Your 1RM is: {results:.2f}")


