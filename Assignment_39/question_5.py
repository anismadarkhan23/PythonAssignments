from fetch_dataset import load_dataset, DATASET_PATH, BORDER
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# I learned the concepts of Trainning accuracy & Testing accuracy and Model underfitting & Model overfitting.
# Trainning Accuracy -> It means, the the model will use the trainning data only and calculate the accuracy.
# Testing Accuracy -> It means, the the model will use the testing data only and calculate the accuracy.
# Underfitting Model -> If both trainning & testing accuracy is low which means model is too simple & it fails on both datasets.
# Overfitting Model -> If trainning accuracy is very high & testing accuracy is low which means model fails on unseen data.
# Observation -> With the student performance dataset the model generates almost 100% trainning accuracy
# and near about 90% testing accuracy with 70% data used for trainning & 30% used for testing.
    # based on this we can say that this model is Good fit.

def check_trainning_accuracy(std_perf_model, X_studyParams_train, Y_resultType_train):
    print("Checking Training Accuracy...")
    y_train_pred = std_perf_model.predict(X_studyParams_train)
    trainning_accuracy = accuracy_score(Y_resultType_train, y_train_pred)
    print("Trainning Accuracy : ", trainning_accuracy * 100, "%")
    print(BORDER)

def check_testing_accuracy(std_perf_model, X_studyParams_test, Y_resultType_test):
    print("Checking Testing Accuracy...")
    y_train_pred = std_perf_model.predict(X_studyParams_test)
    testing_accuracy = accuracy_score(Y_resultType_test, y_train_pred)
    print("Testing Accuracy : ", testing_accuracy * 100, "%")
    print(BORDER)

def train_model(X_studyParams_train, X_studyParams_test, Y_resultType_train, Y_resultType_test):
    std_perf_model = DecisionTreeClassifier()
    std_perf_model.fit(X_studyParams_train, Y_resultType_train)
    print(std_perf_model)
    print("Model trained successfully...")
    print(BORDER)

    check_trainning_accuracy(std_perf_model, X_studyParams_train, Y_resultType_train)
    check_testing_accuracy(std_perf_model, X_studyParams_test, Y_resultType_test)
    
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
