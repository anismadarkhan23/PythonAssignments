import streamlit as st

st.markdown(
    "<h1 style='text-align: center; color: skyblue;'>SIMPLE INTEREST CALCULATOR</h1>", 
    unsafe_allow_html = True
)

col_num_input1, col_num_input2, col_num_input3 = st.columns([1, 1, 1])

principal_amount = col_num_input1.number_input(
    "Enter Principal Amount", 
    value = 0.0,
    step = 0.01,
    format = "%.2f"
)

rate_of_interest = col_num_input2.number_input(
    "Enter Rate of Interest", 
    value = 0.0,
    step = 0.01,
    format = "%.2f"
)

time_period = col_num_input3.number_input(
    "Enter Time Period in years", 
    value = 0,
    step = 1
)

btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 1])

if btn_col2.button("Calculate", use_container_width = True):

    simple_interest = (principal_amount * rate_of_interest * time_period) / 100

    st.markdown(
        f"<h5 style='text-align: center; color: green;'>The simple interest on amount Rs.{principal_amount} with {rate_of_interest}% for {time_period} years is Rs.{simple_interest}</h5>", 
        unsafe_allow_html = True
    )