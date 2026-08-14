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

    # Rename / Replace column name
    stud_marks_df = stud_marks_df.rename(columns = {
        "Math": "Mathematics"
    })

    # Replace particular value from a particular column
    stud_marks_df["Name"] = stud_marks_df["Name"].replace("Pooja", "Puja")

    print(BORDER)
    print("Students marks dataset is")
    print(stud_marks_df.head())
    print(BORDER)


    print(BORDER)

if __name__ == "__main__":
    main()