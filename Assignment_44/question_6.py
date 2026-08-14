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

    stud_marks_df["Total"] = stud_marks_df["Math"] + stud_marks_df["Science"] + stud_marks_df["English"]

    # Sorting the data frame in descending order by comparing Total column
    # by -> column name on basis of that we are going to sort data frame
    # ascending = False -> sorts the data frame in decending order, if sets True it will sorts dataframe in ascending order
    stud_marks_df = stud_marks_df.sort_values(by = "Total", ascending = False)

    print(BORDER)
    print("Students marks dataset is")
    print(stud_marks_df.head())
    print(BORDER)

if __name__ == "__main__":
    main()