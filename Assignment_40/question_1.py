import os

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

DATASET_PATH = "student_performance_ml.csv"
BORDER = "-" * 110

def check_feature_importance(sp_model, feature_names):
    print("Checking feature importance for the model...")
    feature_importance = sp_model.feature_importances_
    feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importance})
    feature_importance_df = feature_importance_df.sort_values(by = 'Importance', ascending = False)
    print(feature_importance_df)
    print(BORDER)

def train_model(X_studyParams_train, Y_resultType_train):
    std_perf_model = DecisionTreeClassifier(max_depth = 3)
    std_perf_model.fit(X_studyParams_train, Y_resultType_train)
    print("Model trained successfully...")
    print(BORDER)

    check_feature_importance(std_perf_model, X_studyParams_train.columns)

def get_independent_dependent_data(data_frame):
    print("Generating independent and dependent data....")

    independent_columns = [
        "StudyHours", 
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
        ]

    study_parameters = data_frame[independent_columns]
    result_type = data_frame["FinalResult"]

    print("Independent and dependent data generated successfully...")
    print(BORDER)
    
    return study_parameters, result_type

def split_train_test_model(studyParams, resultType):
    X_train, X_test, Y_train, Y_test = train_test_split(studyParams, resultType, 
                                                        test_size = 0.5, random_state = 42)
    print("Dataset splitted for building, traning & testing the model...")
    print(BORDER)

    train_model(X_train, Y_train)

def do_ops_for_model_prep(data_frame):
    X_studyParams, y_resultType = get_independent_dependent_data(data_frame)
    split_train_test_model(X_studyParams, y_resultType)

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

    do_ops_for_model_prep(df)

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
