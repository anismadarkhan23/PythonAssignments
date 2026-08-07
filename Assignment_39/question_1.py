from fetch_dataset import load_dataset, DATASET_PATH, BORDER
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def train_model(X_studyParams_train, Y_resultType_train):
    std_perf_model = DecisionTreeClassifier()
    std_perf_model.fit(X_studyParams_train, Y_resultType_train)
    print(std_perf_model)
    print("Model trained successfully...")
    print(BORDER)
    
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

    train_model(X_train, Y_train)

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
