import pandas as pd

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

    # Rename / Replace column name
    stud_marks_df = stud_marks_df.rename(columns = {
        "Math": "Mathematics"
    })

    print(BORDER)
    print("Students marks dataset is")
    print(stud_marks_df)
    print(BORDER)

if __name__ == "__main__":
    main()