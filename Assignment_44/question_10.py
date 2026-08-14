import pandas as pd

def main():
    data = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [85, 90, 78],
        "Science": [92, 88, 80],
        "English": [75, 85, 82]
    }

    stud_marks_df = pd.DataFrame(data)

    stud_marks_df = stud_marks_df.drop(columns=["English"])

    print("After dropping English column:")
    print(stud_marks_df.head())

if __name__ == "__main__":
    main()