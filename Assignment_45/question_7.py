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

    stud_marks_df.to_csv("Student_Marks.csv", index = False)

    print("Eported DataFrame successfully")
    print(BORDER)

if __name__ == "__main__":
    main()