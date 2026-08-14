import pandas as pd
from sklearn.preprocessing import OneHotEncoder

BORDER = "-" * 90

def main():
    data = {
        "Name": ["Amit", "Sagar", "Pooja", "Aarti"],
        "Math": [85, 90, 78, 81],
        "Science": [92, 88, 80, 94],
        "English": [75, 85, 82, 99]
    }

    stud_marks_df = pd.DataFrame(data)

    stud_marks_df["Total"] = stud_marks_df["Math"] + stud_marks_df["Science"] + stud_marks_df["English"]

    stud_marks_df["Gender"] = ["Male", "Male", "Female", "Female"]

    print(BORDER)
    print("Student DataFrame is")
    print(BORDER)
    print(stud_marks_df)
    print(BORDER)

    stud_genderGroup = stud_marks_df.groupby("Gender")[["Math", "Science", "English"]].mean()

    print("Average marks of student by gender group")
    print(BORDER)
    print(stud_genderGroup)
    print(BORDER)

if __name__ == "__main__":
    main()