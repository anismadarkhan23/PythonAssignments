import pandas as pd
from sklearn.preprocessing import OneHotEncoder

BORDER = "-" * 90

def main():
    data = {
        "Name": ["Amit", "Sagar", "Pooja", "Aarti", "Mahesh", "Komal", "Yogesh", "Shraddha"],
        "Math": [85, 90, 78, 81, 56, 70, 18, 91],
        "Science": [92, 88, 80, 94, 67, 69, 12, 78],
        "English": [75, 85, 82, 99, 45, 90, 42, 84]
    }

    stud_marks_df = pd.DataFrame(data)

    stud_marks_df["Total"] = stud_marks_df["Math"] + stud_marks_df["Science"] + stud_marks_df["English"]

    stud_marks_df["Gender"] = ["Male", "Male", "Female", "Female", "Male", "Female", "Male", "Female"]

    for index, total_marks in enumerate(stud_marks_df["Total"]):
        if total_marks >= 250:
            stud_marks_df.at[index, "Status"] = ["Pass"]
        else:
            stud_marks_df.at[index, "Status"] = ["Fail"]

    print(BORDER)
    print("Student Marks with Status")
    print(BORDER)
    print(stud_marks_df)
    print(BORDER)

    passed_student_count = 0
    for status in stud_marks_df["Status"]:
        if status == "Pass":
            passed_student_count += 1

    print("Total passed students are: ", passed_student_count)
    print(BORDER)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------
# Output: 
# ----------------------------------------------------------
# ----------------------------------------------------------
# Student Marks with Status
# ----------------------------------------------------------
#        Name  Math  Science  English  Total  Gender Status
# 0      Amit    85       92       75    252    Male   Pass
# 1     Sagar    90       88       85    263    Male   Pass
# 2     Pooja    78       80       82    240  Female   Fail
# 3     Aarti    81       94       99    274  Female   Pass
# 4    Mahesh    56       67       45    168    Male   Fail
# 5     Komal    70       69       90    229  Female   Fail
# 6    Yogesh    18       12       42     72    Male   Fail
# 7  Shraddha    91       78       84    253  Female   Pass
# ----------------------------------------------------------
# Total passed students are:  4
# ----------------------------------------------------------
# ----------------------------------------------------------