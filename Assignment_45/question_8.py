import pandas as pd
import matplotlib.pyplot as plt

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

    plt.hist(
        stud_marks_df["Math"],
        bins = 5,              
        edgecolor = "black",
        alpha = 0.8,
        rwidth = 0.9
    )

    plt.title("Students Math Marks Histogram")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.show()
    
if __name__ == "__main__":
    main()