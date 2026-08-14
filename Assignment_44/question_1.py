import pandas as pd

BORDER = "-" * 90

def main():
    data = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [85, 90, 78],
        "Science": [92, 88, 80],
        "English": [75, 85, 82]
    }

    stud_marks_df = pd.DataFrame(data)

    print(BORDER)

    print("Dataset is as below")
    print(stud_marks_df.head())

    print(BORDER)

    print("Shape of dataset is : ", stud_marks_df.shape)
    print(BORDER)

    print("Column names of dataset is : ", stud_marks_df.columns)
    print(BORDER)

    print("Datatype of dataset is : ", type(stud_marks_df))
    print(BORDER)

if __name__ == "__main__":
    main()