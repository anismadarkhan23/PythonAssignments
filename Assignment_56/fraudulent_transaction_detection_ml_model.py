import os
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier, BaggingClassifier, AdaBoostClassifier, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

BORDER = "-" * 100

def evaluate_model_with_decision_tree(model_dt, X_train, Y_train, X_test, Y_test):
    model_dt.fit(X_train, Y_train)
    model_predicted_result = model_dt.predict(X_test)
    model_accuracy = accuracy_score(Y_test, model_predicted_result)
    print(BORDER)
    print("------------------------------------- DECISION TREE CLASSIFIER -------------------------------------")
    print(f"Overall Model Accuracy with Decision Tree: {model_accuracy * 100:.2f}%")
    print("------------------------------------- DECISION TREE CLASSIFIER -------------------------------------")
    print(BORDER)

def evaluate_model_with_bagging_classifier(model_bgC, X_train, Y_train, X_test, Y_test):
    model_bgC = model_bgC.fit(X_train, Y_train)
    
    Y_pred = model_bgC.predict(X_test)

    print(BORDER)
    print("---------------------------------------- BAGGING CLASSIFIER ----------------------------------------")
    print(f"Overall Model Accuracy with Bagging Classifier: : {accuracy_score(Y_test, Y_pred) * 100:.2f}%")
    print("---------------------------------------- BAGGING CLASSIFIER ----------------------------------------")
    print(BORDER)

def evaluate_model_with_boosting_classifier(model_bt, X_train, Y_train, X_test, Y_test):
    model_bt = model_bt.fit(X_train, Y_train)

    Y_pred = model_bt.predict(X_test)

    print(BORDER)
    print("---------------------------------------- BOOSTING CLASSIFIER ---------------------------------------")
    print(f"Overall Model Accuracy with Boosting Classifier: : {accuracy_score(Y_test, Y_pred) * 100:.2f}%")
    print("---------------------------------------- BOOSTING CLASSIFIER ---------------------------------------")
    print(BORDER)

def evaluate_model_with_random_forest_classifier(model_rf, X_train, Y_train, X_test, Y_test):
    model_rf = model_rf.fit(X_train, Y_train)

    Y_pred = model_rf.predict(X_test)

    print(BORDER)
    print("---------------------------------------- RANDOM FOREST CLASSIFIER ----------------------------------")
    print(f"Overall Model Accuracy with Boosting Classifier: : {accuracy_score(Y_test, Y_pred) * 100:.2f}%")
    print("---------------------------------------- RANDOM FOREST CLASSIFIER ----------------------------------")
    print(BORDER)

def voting_classifier_customer_loan_approval_model(X_train, X_test, Y_train, Y_test, model_dt, model_bgC, model_bt, model_rf, vote_type):
    print(BORDER)
    print(BORDER)
    print("------------------------------------- Hard Voting Classifier Model ---------------------------------")
    print("Creating a Voting Classifier model...")
    model_vc = VotingClassifier(
        estimators = [
            ('dt', model_dt),
            ('bc', model_bgC),
            ('bt', model_bt),
            ('rf', model_rf)
        ],
        voting = vote_type
    )
    model_vc.fit(X_train, Y_train)

    Y_pred = model_vc.predict(X_test)

    print("Evaluating the model performance...")
    model_accuracy = accuracy_score(Y_test, Y_pred)
    print(f"Overall Model Accuracy with Hard voting classifier: {model_accuracy * 100:.2f}%")
    print(BORDER)
    print("------------------------------------- Hard Voting Classifier Model ---------------------------------")

    print("----------------------------------------- CLASSIFICATION REPORT ------------------------------------")
    print(BORDER)
    print("Classification Report for Decision Tree Classifier")
    print(classification_report(Y_test, Y_pred))
    print(BORDER)
    print("----------------------------------------- CLASSIFICATION REPORT ------------------------------------")

def fraudulent_transaction_detection_model(DATASET_PATH):
    if not os.path.exists(DATASET_PATH):
        print(f"Dataset file '{DATASET_PATH}' not found.")
        print(BORDER)
        return

    data_frame = pd.read_csv(DATASET_PATH)

    print(BORDER)
    print("Dataset loaded successfully...")
    print(BORDER)

    if len(data_frame.shape) == 0:
        print("No data found in dataset")
        print(BORDER)
        return
    else:
        print("Shape of Dataset: ", data_frame.shape)
        print(BORDER)

        print("First 10 records of the dataset to understand the data")
        print(data_frame.head(10))
        print(BORDER)

    if data_frame.isnull().values.any():
        if data_frame.isnull().sum().sum() > 0:
            print("Dataset has missing values. Cleaning the dataset before proceeding further.")
            data_frame = data_frame.dropna()

            print("Dataset cleaned successfully...")
            print(BORDER)
    else:
        print("Performing Exploratory Data Analysis (EDA) on the dataset to check \nmissing values, data types, and statistical summary of the dataset")
        print(BORDER)

        print("No missing values found in the dataset.")
        print(data_frame.info())
        print(BORDER)

    print("Checking the distribution of classes of target columns in the dataset")
    print(BORDER)
    print(data_frame["Fraud"].value_counts())
    print(BORDER)

    print(data_frame["DeviceType"].value_counts())
    print(BORDER)
    
    print("Generating independent and dependent data....")
    print(BORDER)

    features_columns = data_frame.drop("Fraud", axis=1)
    label_column = data_frame["Fraud"]

    print("Independent features columns: ")
    for col_name in list(features_columns.columns):
        print(col_name)
    print(BORDER)

    print("Dependent label column: ", label_column.name)
    print(BORDER)

    print("Splitting the dataset into training and testing sets...")
    X_train, X_test, Y_train, Y_test = train_test_split(features_columns, label_column, test_size = 0.5, random_state = 42)

    print("Dataset splitted for building, training & testing the model...")
    print(BORDER)

    print("Shape of training features: ", X_train.shape)
    print("Shape of testing features: ", X_test.shape)
    print("Shape of training labels: ", Y_train.shape)
    print("Shape of testing labels: ", Y_test.shape)
    print(BORDER)

    print("Scaling the features for better model performance...")
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print("Features scaled successfully...")
    print("Scaled training data:")
    print(pd.DataFrame(X_train).head())
    print(BORDER)
    print("Scaled testing data:")
    print(pd.DataFrame(X_test).head())
    print(BORDER)

    model_dt = DecisionTreeClassifier(random_state = 42)
    evaluate_model_with_decision_tree(model_dt, X_train, Y_train, X_test, Y_test)

    model_bgC = BaggingClassifier(
        estimator = model_dt,
        n_estimators = 10,
        random_state = 42
    )
    evaluate_model_with_bagging_classifier(model_bgC, X_train, Y_train, X_test, Y_test)

    model_bt = AdaBoostClassifier(
        n_estimators = 50,
        learning_rate = 1.0,
        random_state = 42 
    )
    evaluate_model_with_boosting_classifier(model_bt, X_train, Y_train, X_test, Y_test)

    model_rf = RandomForestClassifier(
        n_estimators = 10,
        random_state = 42 
    )
    evaluate_model_with_random_forest_classifier(model_rf, X_train, Y_train, X_test, Y_test)

    voting_classifier_customer_loan_approval_model(X_train, X_test, Y_train, Y_test, model_dt, model_bgC, model_bt, model_rf, "hard")

def main():
    fraudulent_transaction_detection_model("Fraudulent_Transaction_Detection.csv")

if __name__ == "__main__":
    main()