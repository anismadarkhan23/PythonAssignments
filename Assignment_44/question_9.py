import pandas as pd
import numpy as np

def main():
    data = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [np.nan, 90, 78],
        "Science": [92, np.nan, 80],
        "English": [75, 85, np.nan]
    }

    stud_marks_df = pd.DataFrame(data)
    print("-" * 80)
    print("Before replacing NaN values with mean:")
    print(stud_marks_df.head())
    print("-" * 80)

    mean_of_math = stud_marks_df["Math"].mean()
    mean_of_science = stud_marks_df["Science"].mean()
    mean_of_english = stud_marks_df["English"].mean()

    stud_marks_df["Math"] = stud_marks_df["Math"].replace(np.nan, mean_of_math)
    stud_marks_df["Science"] = stud_marks_df["Science"].replace(np.nan, mean_of_science)
    stud_marks_df["English"] = stud_marks_df["English"].replace(np.nan, mean_of_english)

    print("-" * 80)
    print("After replacing NaN values with mean:")
    print(stud_marks_df.head())
    print("-" * 80)

if __name__ == "__main__":
    main()