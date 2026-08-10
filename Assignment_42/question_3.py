import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
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

    study_hours = int(input("Enter the study hours: "))
    attendance_percentage = int(input("Enter the attendance percentage: "))
    test_stud_data = {
        "Study Hours" : [study_hours],
        "Attendance" : [attendance_percentage]
    }

    test_stud_data = pd.DataFrame(test_stud_data)

    print("Testing student data as below")
    print(test_stud_data)
    print(BORDER)

    print("Seperated dependent & independet variables")
    X = df.drop(columns = ["Result"])
    Y = df["Result"]
    print(BORDER)

    print("Trained the model")
    model = KNeighborsClassifier(n_neighbors = 3)
    model = model.fit(X, Y)
    print(BORDER)

    print("Tested the model & calculated the accuracy")
    model.predict(test_stud_data)
    predicted_result = model.predict_proba(test_stud_data)
    print(BORDER)

    probability = float(f"{predicted_result[0][1] * 100:.2f}")
    print("Model prediction: ", "Student will fail" if probability < 66.67 else "Student will pass")
    print(BORDER)

def main():
    predict_student_result(3)

if __name__ == "__main__":
    main()
