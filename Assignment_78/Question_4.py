import streamlit as st

st.markdown(
    "<h1 style='text-align: center; color: skyblue;'>STUDENT RESULT CALCULATOR</h1>", 
    unsafe_allow_html = True
)

student_name = st.text_input(
    "Enter Student Name"
)

maths_marks = st.number_input(
    "Enter Marks Obtained in Maths", 
    value = 0
)

science_marks = st.number_input(
    "Enter Marks Obtained in Science", 
    value = 0
)

english_marks = st.number_input(
    "Enter Marks Obtained in English", 
    value = 0
)

btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 1])

if btn_col2.button("Calculate Result", use_container_width = True):

    total_marks = maths_marks + science_marks + english_marks

    st.text_input(
        "Total Marks",
        value = total_marks,
        disabled = True
    )

    percentage = total_marks / 3

    st.text_input(
        "Percentage",
        value = f"{percentage:.2f}%",
        disabled = True
    )

    if (maths_marks < 40 or science_marks < 40 or english_marks < 40) or (percentage < 40):
        st.markdown(
            f"<h5 style='text-align: center; color: red;'>{student_name} is failed in exam</h5>", 
            unsafe_allow_html = True
        )
    else:
        st.markdown(
            f"<h5 style='text-align: center; color: green;'>{student_name} is passed in exam</h5>",
            unsafe_allow_html = True
        )