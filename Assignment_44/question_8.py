import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [85, 90, 78],
        "Science": [92, 88, 80],
        "English": [75, 85, 82]
    }

    stud_marks_df = pd.DataFrame(data)
    stud_marks_df["Total"] = stud_marks_df["Math"] + stud_marks_df["Science"] + stud_marks_df["English"]

    subject_names = list()
    for subject in data:
        if subject == "Name":
            continue
        subject_names.append(subject)

    print(subject_names)

    stud_marks = list()
    for name in stud_marks_df["Name"]:
        if name == "Amit":
            temp = stud_marks_df[stud_marks_df["Name"] == name]
            temp.drop(columns=["Name", "Total"], inplace = True)
            stud_marks.append(temp[subject_names].values[0])
            
    print(stud_marks[0])

    plt.plot(
        subject_names,
        stud_marks[0],
        marker = "o",
        linestyle = "--",
        linewidth = 2,
        markersize = 7,
        label = "Marks"
    )

    plt.title("Marvellous Line Plot")
    plt.xlabel("Student Number")
    plt.ylabel("Marks")

    plt.grid(True)

    plt.legend()

    plt.show()

if __name__ == "__main__":
    main()
