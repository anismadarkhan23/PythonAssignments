from fetch_dataset import load_dataset, DATASET_PATH, BORDER
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def display_confusion_matrix(model_predicted_result, Y_resultType_test):
    print("Confusion Matrix")
    print(confusion_matrix(Y_resultType_test, model_predicted_result))
    print(BORDER)
    print("True positive -> " \
        "The model which predicts correct positive samples. " \
        "Which means, if student is passed (1) then \n" \
        "this model has predicted it as passed (1) " \
        "only which is True positive")
    print(BORDER)
    print("True negative -> "
        "The model which predicts correct negative samples. " \
        "Which means, if student is failed (0) then \n" \
        "this model has predicted it as failed (0) " \
        "only which is True negative")
    print(BORDER)
    print("False positive -> "
        "The model which predicts incorrect positive samples. " \
        "Which means, if student is passed (1) \n" \
        "then this model has predicted it as failed (0) " \
        "only which is False positive")
    print(BORDER)
    print("False negative -> "
        "The model which predicts incorrect negative samples. " \
        "Which means, if student is failed (0) \n" \
        "then this model has predicted it as passed (1) " \
        "only which is False negative")
    print(BORDER)
        

def check_model_accuracy(model_predicted_result, Y_resultType_test):
    model_accuracy = accuracy_score(Y_resultType_test, model_predicted_result)
    print("Model Accuracy : ", model_accuracy * 100, "%")
    print(BORDER)

    display_confusion_matrix(model_predicted_result, Y_resultType_test)

def display_predicted_and_actual_result(model_predicted_result, Y_resultType_test):
    print("Predicted result : ", model_predicted_result)
    print("Actual result : ", list(Y_resultType_test))
    print(BORDER)

    check_model_accuracy(model_predicted_result, Y_resultType_test)

def test_model(std_perf_model, X_studyParams_test, Y_resultType_test):
    model_predicted_result = std_perf_model.predict(X_studyParams_test)
    print("Model testing completed successfully...")
    print(BORDER)

    display_predicted_and_actual_result(model_predicted_result, Y_resultType_test)

def train_model(X_studyParams_train, X_studyParams_test, Y_resultType_train, Y_resultType_test):
    std_perf_model = DecisionTreeClassifier()
    std_perf_model.fit(X_studyParams_train, Y_resultType_train)
    print(std_perf_model)
    print("Model trained successfully...")
    print(BORDER)

    test_model(std_perf_model, X_studyParams_test, Y_resultType_test)
    
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
                                                        test_size = 0.3, random_state = 42)
    print("Dataset splitted for building, traning & testing the model...")
    print(BORDER)

    train_model(X_train, X_test, Y_train, Y_test)

def do_ops_for_model_prep(data_frame):
    X_studyParams, y_resultType = get_independent_dependent_data(data_frame)
    split_train_test_model(X_studyParams, y_resultType)

def do_data_analysis():
    df = load_dataset(DATASET_PATH)

    print(BORDER)
    print("Checking missing values per column...")
    print(df.isnull().sum())
    print(BORDER)
    print("Checking class distribution...")
    print("Class distribution (FinalResult count)")
    print(df["FinalResult"].value_counts())
    print(BORDER)
    print("Generating stastical report of dataset...")
    print("Stastical report of dataset is as below ")
    print(df.describe())
    print(BORDER)

    do_ops_for_model_prep(df)

def main():
    do_data_analysis()

if __name__ == "__main__":
    main()
