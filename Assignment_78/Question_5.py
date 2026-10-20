import streamlit as st

st.markdown(
    "<h1 style='text-align: center; color: skyblue;'>CELCIUS TO FAHRENHEIT CONVERTER</h1>", 
    unsafe_allow_html = True
)

cel_temp = st.number_input(
    "Enter temprature in Celcius", 
    value = 0.0,
    format = "%.2f"
)

btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 1])

if btn_col2.button("Convert", use_container_width = True):

    result = (cel_temp * 1.8) + 32

    st.info(
        f"Temprature in Fahrenheit is {result}°F"
    )