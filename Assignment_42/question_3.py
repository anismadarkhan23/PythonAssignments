import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

BORDER = "-" * 55

def predict_student_result(k_neighbour):

    student_data = {
            "Study Hours" : [2, 5, 6, 1], 
            "Attendance" : [60, 80, 85, 50], 
            "Result" : ["Fail", "Pass", "Pass", "Fail"]
        }

    df = pd.DataFrame(student_data)

    print(BORDER)
    print("Given student result data as below")
    print(BORDER)

    print(df.head())

    print(BORDER)

    print("Seperated dependent & independet variables")
    X = df.drop(columns = ["Result"])
    Y = df["Result"].map(
        {"Fail": 0, "Pass": 1}
    )
    print(BORDER)

    print("Scaling the data")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print(BORDER)

    print("Trained the model")
    model = KNeighborsClassifier(n_neighbors = k_neighbour)
    model = model.fit(X_scaled, Y)
    print(BORDER)

    study_hours = int(input("Enter the study hours: "))
    attendance_percentage = int(input("Enter the attendance percentage: "))
    test_stud_data = {
        "Study Hours" : [study_hours],
        "Attendance" : [attendance_percentage]
    }

    test_stud_data = pd.DataFrame(test_stud_data)
    test_stud_data_scaled = scaler.transform(test_stud_data)

    print("Tested the model & predicted the result")
    predicted_result = model.predict(test_stud_data_scaled)
    print(BORDER)
    print("Model prediction: ", "Pass" if predicted_result[0] == 1 else "Fail")
    print(BORDER)

def main():
    predict_student_result(3)

if __name__ == "__main__":
    main()
