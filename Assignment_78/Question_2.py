import streamlit as st

st.markdown(
    "<h1 style='text-align: center; color: skyblue;'>EVEN OR ODD NUMBER CHECKER</h1>", 
    unsafe_allow_html = True
)

num = st.number_input(
    "Enter the number to check whether the number is even or odd", 
    value = 0
)

btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 1])

if btn_col2.button("Check", use_container_width = True):

    if num % 2 == 0:
        color = "green"
        result = "Entered number is even"
    else:
        color = "red"
        result = "Entered number is odd"

    st.markdown(
        f"<h4 style='text-align: center; color: {color};'>{result}</h4>", 
        unsafe_allow_html = True
    )