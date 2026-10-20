import streamlit as st

st.markdown(
    "<h1 style='text-align: center; color: skyblue;'>Addition Calculator</h1>", 
    unsafe_allow_html = True
)

col_num_input1, col_num_input2 = st.columns([0.5, 0.5])

no1 = col_num_input1.number_input(
    "Enter first number: ", 
    value = 0,
    step = 1
)

no2 = col_num_input2.number_input(
    "Enter second number: ", 
    value = 0, 
    step = 1
)

btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 1])


if btn_col2.button("Addition", use_container_width = True):
    result = no1 + no2

    btn_col2.markdown(
        f"<h4 style='text-align: center; color: green;'>Addition is {result}</h4>", 
        unsafe_allow_html=True
    )