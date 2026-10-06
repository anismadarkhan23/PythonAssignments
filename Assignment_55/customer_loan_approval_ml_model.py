import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

BORDER = "-" * 100
DATASET_PATH = "Customer_Loan_Approval.csv"

def test_model_with_unseen_data(model_vc, scaler):
    print("Test the model with a sample input to predict loan approval...")
    income = float(input("Enter the income of the customer: "))
    credit_score = float(input("Enter the credit score of the customer: "))
    existing_loans = float(input("Enter the existing loan amounts for the customer: "))
    loan_amount = float(input("Enter the loan amount requested by the customer: "))

    customer_data = pd.DataFrame([{
        "Income": income,
        "CreditScore": credit_score,
        "ExistingLoan": existing_loans,
        "LoanAmount": loan_amount
    }])

    print(BORDER)

    customer_data = scaler.transform(customer_data)

    result = model_vc.predict(customer_data)

    if result[0] == 1:
        print("The loan is approved for the customer.")
    else:
        print("The loan is rejected for the customer.")

def evaluate_model_with_logistic_regression(model_lr, X_train, Y_train, X_test, Y_test):
    model_lr.fit(X_train, Y_train)
    model_predicted_result = model_lr.predict(X_test)
    model_accuracy = accuracy_score(Y_test, model_predicted_result)
    print(f"Overall Model Accuracy with Logistic Regression: {model_accuracy * 100:.2f}%")
    print(BORDER)

def evaluate_model_with_decision_tree(model_dt, X_train, Y_train, X_test, Y_test):
    model_dt.fit(X_train, Y_train)
    model_predicted_result = model_dt.predict(X_test)
    model_accuracy = accuracy_score(Y_test, model_predicted_result)
    print(f"Overall Model Accuracy with Decision Tree: {model_accuracy * 100:.2f}%")
    print(BORDER)

def evaluate_model_with_knn(model_knn, X_train, Y_train, X_test, Y_test):
    model_knn.fit(X_train, Y_train)
    model_predicted_result = model_knn.predict(X_test)
    model_accuracy = accuracy_score(Y_test, model_predicted_result)
    print(f"Overall Model Accuracy with K-Nearest Neighbors: {model_accuracy * 100:.2f}%")
    print(BORDER)

def voting_classifier_customer_loan_approval_model(scaler, X_train, X_test, Y_train, Y_test, model_lr, model_dt, model_knn, vote_type):
    print(BORDER)
    print(BORDER)
    print(f"----------------------------------- {vote_type.capitalize()} Voting Classifier Model -----------------------------------")
    print("Creating a Voting Classifier model...")
    model_vc = VotingClassifier(
        estimators = [
            ('lr', model_lr),
            ('dt', model_dt),
            ('knn', model_knn)
        ],
        voting = vote_type
    )
    model_vc.fit(X_train, Y_train)

    model_predicted_result = model_vc.predict(X_test)

    print("Evaluating the model performance...")
    model_accuracy = accuracy_score(Y_test, model_predicted_result)
    print(f"Overall Model Accuracy with {vote_type.capitalize()} voting classifier: {model_accuracy * 100:.2f}%")
    print(BORDER)

    test_model_with_unseen_data(model_vc, scaler)

    print(f"----------------------------------- {vote_type.capitalize()} Voting Classifier Model -----------------------------------")

def customer_load_approval_model(dataset_path):
    if not os.path.exists(DATASET_PATH):
        print(f"Dataset file '{DATASET_PATH}' not found.")
        print(BORDER)
        return
    
    data_frame = pd.read_csv(dataset_path)

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

    print("Checking the distribution of classes of target column in the dataset")
    print(BORDER)
    print(data_frame["LoanApproved"].value_counts())
    print(BORDER)

    print("Generating independent and dependent data....")
    print(BORDER)

    features_columns = data_frame.drop(["Age", "EmploymentExperience", "LoanApproved"], axis=1)
    label_column = data_frame["LoanApproved"]

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
    print(BORDER)

    print("Creating individual models for Logistic Regression, Decision Tree, and K-Nearest Neighbors...")
    model_logReg = LogisticRegression(max_iter = 2500)
    model_dt = DecisionTreeClassifier(random_state = 42)
    model_knn = KNeighborsClassifier(n_neighbors = 3)
    print("Individual models created successfully...")
    print(BORDER)

    evaluate_model_with_logistic_regression(model_logReg, X_train, Y_train, X_test, Y_test)
    
    evaluate_model_with_decision_tree(model_dt, X_train, Y_train, X_test, Y_test)
    evaluate_model_with_knn(model_knn, X_train, Y_train, X_test, Y_test)

    voting_classifier_customer_loan_approval_model(scaler, X_train, X_test, Y_train, Y_test, 
                                             model_logReg, model_dt, model_knn, vote_type = "hard")

    voting_classifier_customer_loan_approval_model(scaler, X_train, X_test, Y_train, Y_test, 
                                                 model_logReg, model_dt, model_knn, vote_type = "soft")
    
    
    print(BORDER)
    print(BORDER)

def main():
    customer_load_approval_model(DATASET_PATH)

if __name__ == "__main__":
    main()