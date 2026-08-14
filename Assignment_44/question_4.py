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

    print(BORDER)
    print("Students marks dataset is")
    print(stud_marks_df.head())
    print(BORDER)

    print("Students who scored more than 85 in science are: ")
    for name in stud_marks_df["Name"]:
        temp = stud_marks_df[stud_marks_df["Name"] == name]
        for s_marks in temp["Science"]:
            if s_marks > 85:
                print(name)

    print(BORDER)

if __name__ == "__main__":
    main()