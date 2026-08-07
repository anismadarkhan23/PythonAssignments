import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

DATASET_PATH = "student_performance_ml.csv"
BORDER = "-" * 110

def test_model(sp_model, 
               X_perfParams_train, 
               X_perfParams_test, 
               Y_resultType_train, 
               Y_resultType_test):

    model_predicted_classes = sp_model.predict(X_perfParams_test)
    model_predicted_prob = sp_model.predict_proba(X_perfParams_test)
    print("Model testing completed successfully for single random student record...")
    for i in range(len(model_predicted_prob)):
        if model_predicted_prob[i][1] > 0.5:
            print("Probability of student to pass the exam is: ", model_predicted_prob[i][1] * 100, "%", model_predicted_classes[i])
        else:
            print("Probability of student to fail the exam is: ", model_predicted_prob[i][0] * 100, "%", model_predicted_classes[i])
    print(BORDER)

def train_model(X_perfParams_train, 
                X_perfParams_test, 
                Y_resultType_train, 
                Y_resultType_test):

    sp_model = DecisionTreeClassifier(max_depth = 5)

    sp_model.fit(X_perfParams_train, Y_resultType_train)

    print("Model trained successfully...")
    print(BORDER)

    studentPerf_data = {
            "StudyHours" : [6, 2, 4, 8, 5], 
            "Attendance" : [85, 60, 75, 90, 80], 
            "PreviousScore" : [66, 55, 70, 85, 75], 
            "AssignmentsCompleted" : [7, 4, 5, 9, 6], 
            "SleepHours" : [7, 5, 6, 8, 7]
        }
    X_studentPerf_test = pd.DataFrame(studentPerf_data)

    test_model(sp_model, X_perfParams_train, X_studentPerf_test, Y_resultType_train, Y_resultType_test)

def get_independent_dependent_data(df):
    print("Generating independent and dependent data....")

    independent_columns = [
        "StudyHours", 
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]

    perf_parameters = df[independent_columns]

    result_type = df["FinalResult"]

    print("Independent and dependent data generated successfully...")
    print(BORDER)

    return perf_parameters, result_type

def split_train_test_model(perfParams, resultType):

    X_train, X_test, Y_train, Y_test = train_test_split(perfParams, resultType, 
                                                        test_size = 0.5, random_state = 42)
    
    print("Dataset splitted for building, traning & testing the model...")
    print(BORDER)

    train_model(X_train, X_test, Y_train, Y_test)

def do_ops_for_model_prep(df):

    X_perfParams, Y_resultType = get_independent_dependent_data(df)

    split_train_test_model(X_perfParams, Y_resultType)

def check_class_distribution(df):
    print("Checking class distribution...")
    print("Class distribution (FinalResult)")

    print(df["FinalResult"].value_counts())

    print(BORDER)

    do_ops_for_model_prep(df)

def do_data_analysis(df):

    print(BORDER)
    print("Checking missing values per column...")

    if not df.isnull().values.any():
        print("Dataset has no missing values. Proceeding further...")
        print(BORDER)

    elif df.isnull().sum().sum() > 0:
        print("Dataset has missing values. Cleaning the dataset before proceeding further...")

        df = df.dropna()

        print("Dataset cleaned successfully...")
        print(BORDER)

    print("Column names: ", list(df.columns))
    print(BORDER)

    check_class_distribution(df)

def load_dataset(file_path):
    data_frame = pd.read_csv(file_path)
    print(f"Dataset loaded successfully from path {os.path.abspath(file_path)}")

    do_data_analysis(data_frame)

def main():
    if not os.path.exists(DATASET_PATH):
        print("Dataset file not found at path: ", DATASET_PATH)
        print(BORDER)
    else:
        load_dataset(DATASET_PATH)

if __name__ == "__main__":
    main()
