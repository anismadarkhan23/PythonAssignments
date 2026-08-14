import pandas as pd
from sklearn.preprocessing import MinMaxScaler

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

    scaler = MinMaxScaler()
    stud_marks_df["Math_Scaled"] = scaler.fit_transform(stud_marks_df[["Math"]])

    print(BORDER)
    print("Scaled Maths scores are")
    print(BORDER)
    print(stud_marks_df)
    print(BORDER)

if __name__ == "__main__":
    main()

# Output
# ------------------------------------------------------
# Scaled Maths scores are
# ------------------------------------------------------
#     Name  Math  Science  English  Total  Math_Scaled
# 0   Amit    85       92       75    252     0.583333
# 1  Sagar    90       88       85    263     1.000000
# 2  Pooja    78       80       82    240     0.000000
# ------------------------------------------------------
# As scaling has been defined from min 0.0 to max 1.0 
# Here, Math_Scaled column indicates that, 
# 0.000 -> Pooja has lowest score in Math
# 0.583 -> Amit has average score in Math which is in between of Sagar & Poojs
# 1.000 -> Sagar has highest score in Math.