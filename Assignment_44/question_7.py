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

    plt.bar(
        stud_marks_df["Name"],
        stud_marks_df["Total"],
        width = 0.6,
        edgecolor = "black",
        linewidth = 1,
        alpha = 0.8,
        label = "Students"
    )

    plt.title("Student Marks Bar Plot")
    plt.xlabel("Student Names")
    plt.ylabel("Total Marks")

    plt.grid(False)
    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    main()