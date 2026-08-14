import pandas as pd
from sklearn.preprocessing import OneHotEncoder

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

    stud_marks_df["Gender"] = ["Male", "Male", "Female"]

    print(BORDER)
    print("Student DataFrame is")
    print(BORDER)
    print(stud_marks_df)
    print(BORDER)

    # Initialize the Encoder
    # sparse_output=False returns a standard NumPy array instead of a sparse matrix
    oh_encodeObj = OneHotEncoder(sparse_output = False)

    # Fit and transform the categorical Gender column
    encoded_genderData = oh_encodeObj.fit_transform(stud_marks_df[["Gender"]])

    # Convert back to DataFrame with column names
    encoded_studDataFrame = pd.DataFrame(encoded_genderData, columns = oh_encodeObj.get_feature_names_out(["Gender"]))

    # Combine with the original DataFrame
    final_stud_df = pd.concat([stud_marks_df, encoded_studDataFrame], axis = 1)

    print(BORDER)
    print("After performing One-Hot Encoding on Gender column")
    print(BORDER)
    print(final_stud_df)
    print(BORDER)

if __name__ == "__main__":
    main()

# Output
# ------------------------------------------------------------------------------------------
# Student DataFrame is
# ------------------------------------------------------------------------------------------
#     Name  Math  Science  English  Total  Gender
# 0   Amit    85       92       75    252    Male
# 1  Sagar    90       88       85    263    Male
# 2  Pooja    78       80       82    240  Female
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# After performing One-Hot Encoding on Gender column
# ------------------------------------------------------------------------------------------
#     Name  Math  Science  English  Total  Gender  Gender_Female  Gender_Male
# 0   Amit    85       92       75    252    Male            0.0          1.0
# 1  Sagar    90       88       85    263    Male            0.0          1.0
# 2  Pooja    78       80       82    240  Female            1.0          0.0
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# OneHotEncoder Eplaination
# ------------------------------------------------------------------------------------------
# 1. Encode categorical features as a one-hot numeric array.
# 2. The input to this transformer should be an array-like of integers or strings, denoting the 
# values taken on by categorical (discrete) features. The features are encoded using a one-hot 
# encoding scheme. 
# 3. This creates a binary column for each category and returns a sparse matrix 
# or dense array (depending on the sparse_output parameter).
# 4. By default, the encoder derives the categories based on the unique values in each feature. 
# Alternatively, you can also specify the categories manually.
# 5. This encoding is needed for feeding categorical data to many scikit-learn estimators, notably 
# linear models and SVMs with the standard kernels.
# ------------------------------------------------------------------------------------------