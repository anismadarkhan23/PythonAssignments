import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = {
        "Name": ["Amit", "Sagar", "Pooja", "Aarti"],
        "Math": [85, 95, 78, 81],
        "Science": [92, 43, 80, 94],
        "English": [75, 41, 82, 99]
    }

    stud_marks_df = pd.DataFrame(data)
    stud_marks_df["Total"] = stud_marks_df["Math"] + stud_marks_df["Science"] + stud_marks_df["English"]
    stud_marks_df["Gender"] = ["Male", "Male", "Female", "Female"]

    subject_names = list()
    for subject in data:
        if subject == "Name":
            continue
        subject_names.append(subject)

    stud_marks = list()
    for name in stud_marks_df["Name"]:
        if name == "Sagar":
            temp = stud_marks_df[stud_marks_df["Name"] == name]
            temp.drop(columns=["Name", "Total"], inplace = True)
            stud_marks.append(temp[subject_names].values[0])

    plt.pie(
        stud_marks[0], # Marks of all subjects
        labels = subject_names, # Subject labels
        autopct = "%.2f%%", # Displays percentages on slices
        startangle = 270, # Rotates the start of the pie chart
        explode = (0.1, 0, 0) # Highlights/pulls out the 'Math' slice
    )

    plt.title("Marvellous Pie Chart")
    plt.show()

if __name__ == "__main__":
    main()
