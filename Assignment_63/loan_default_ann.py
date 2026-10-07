import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

FILE_NAME = "Loan_Default.csv"
BORDER = "-"*175

def create_unseen_emp_attrition_data():
    print("Enter the Applicant's details")
    employees = []

    for i in range(2):
        if i == 0:
            print(f"Enter the details of {i+1}st applicant")
        else:
            print(f"Enter the details of {i+1}nd applicant")

        monthly_income = float(input("Enter applicant's monthly income: "))
        loan_amount = float(input("Enter applicant's loan amount: "))
        credit_score = float(input("Enter applicant's credit score: "))
        employment_years = float(input("Enter applicant's employement years: "))
        existing_loans = float(input("Enter applicant's existing loans: "))
        monthly_debt = float(input("Enter applicant's monthly debt: "))
        loan_term = float(input("Enter applicant's loan term: "))
        previous_default_response = input("Does the applicant previous default? Enter Yes or No: ").strip().lower()
        if previous_default_response not in {"yes", "no"}:
            raise ValueError("Previous default must be entered as Yes or No.")
        previous_default = 1 if previous_default_response == "yes" else 0

        home_ownership_response = input("Applicant's home ownership? Enter Own/Rent/Mortgage: ").strip().lower()
        if home_ownership_response not in {"own", "rent", "mortgage"}:
            raise ValueError("Applicant's home ownership must be entered as Own or Rent or Mortgage.")
        if home_ownership_response == "rent":
            home_ownership = 1
        elif home_ownership_response == "mortgage":
            home_ownership = 2
        else:
            home_ownership = 3
    
        employees.append({
            "Income": monthly_income,
            "LoanAmount": loan_amount,
            "CreditScore": credit_score,
            "EmploymentYears": employment_years,
            "ExistingLoans": existing_loans,
            "MonthlyDebt": monthly_debt,
            "LoanTerm": loan_term,
            "PreviousDefault": previous_default,
            "HomeOwnership": home_ownership
        })

        print(BORDER)

    return pd.DataFrame(employees)

def predict_unseen_employee_attrition(model, scaler):
    employee_data = create_unseen_emp_attrition_data()

    employee_data_scaled = scaler.transform(employee_data)

    predictions = model.predict(employee_data_scaled)
    employee_data["DefaultRisk"] = pd.Series(predictions).map({1: "High", 0: "Low"})

    print("Loan Default Prediction for the entered applicant's")
    print(employee_data.to_string(index=False))
    print(BORDER)

def evaluate_the_model(model, X_train_scaled, X_test_scaled, Y_train, Y_test):
    predicted_result = model.predict(X_test_scaled)

    model_training_accuracy = model.score(X_train_scaled, Y_train)
    print(f"Model training accuracy is: {model_training_accuracy * 100:.2f}%")
    print(BORDER)

    model_testing_accuracy = model.score(X_test_scaled, Y_test)
    print(f"Model testing accuracy is: {model_testing_accuracy * 100:.2f}%")
    print(BORDER)

    model_overall_accuracy = accuracy_score(Y_test, predicted_result)
    print(f"Model overall accuracy is: {model_overall_accuracy * 100:.2f}%")
    print(BORDER)

    cm = confusion_matrix(Y_test, predicted_result)
    print("Confusion Matrix")
    print(cm)
    print(BORDER)

    print("Classification Report")
    print(classification_report(Y_test, predicted_result))
    print(BORDER)

def plot_loss_curve(model):
    losses = model.loss_curve_
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, len(losses) + 1), losses, label="Training loss")
    plt.xlabel("Iterations")
    plt.ylabel("Loss")
    plt.title("Training Loss")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def create_fnn_model_and_train_the_model(X_train_scaled, X_test_scaled, Y_train, Y_test, scaler):
    model = MLPClassifier(
        hidden_layer_sizes = (100, 50, 25),
        activation = 'identity',
        solver = 'adam',
        max_iter = 1000,
        random_state = 42   
    )

    print("FNN Model gets created")
    print(model)
    print(BORDER)

    print("Train the model")
    model.fit(X_train_scaled, Y_train)
    print("Model trainning completed")
    print(BORDER)

    plot_loss_curve(model)
    
    evaluate_the_model(model, X_train_scaled, X_test_scaled, Y_train, Y_test)
    predict_unseen_employee_attrition(model, scaler)

def perform_feature_scaling_on_data(X_train, X_test, Y_train, Y_test):
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("Feature scaling performed on dataset successfully...")
    print(BORDER)

    print("Scaled Training Data")
    print(X_train_scaled[:5])
    print(BORDER)

    print("Scaled Testing Data")
    print(X_test_scaled[:5])
    print(BORDER)

    create_fnn_model_and_train_the_model(X_train_scaled, X_test_scaled, Y_train, Y_test, scaler)

def split_train_test_data(input_features, target_label):
    X_train, X_test, Y_train, Y_test = train_test_split(input_features, target_label, train_size = 0.5, random_state = 42)

    print(BORDER)
    print("Training Input's Shape: ", X_train.shape)
    print(BORDER)

    print("Testing Input's Shape: ", X_test.shape)
    print(BORDER)

    print("Training Output's Shape: ", Y_train.shape)
    print(BORDER)

    print("Testing Output's Shape: ", Y_test.shape)
    print(BORDER)

    perform_feature_scaling_on_data(X_train, X_test, Y_train, Y_test)

def seperate_features_and_labels(df):
    X_features = df.drop(["Age", "Default"], axis = 1)
    Y_labels = df["Default"]

    print(BORDER)
    print("Input Features are")
    print(X_features.head())

    print(BORDER)
    print("Target Labels are")
    print(Y_labels.head())

    split_train_test_data(X_features, Y_labels)

def check_classes_distribution(df):
    print("Checking the distribution of classes in the dataset")
    
    print(BORDER)
    print(df["Default"].value_counts())
    print(BORDER)

    print(df["PreviousDefault"].value_counts())
    print(BORDER)

    print(df["HomeOwnership"].value_counts())
    print(BORDER)

    df["PreviousDefault"] = df["PreviousDefault"].map({"Yes": 1, "No": 0})

    df["HomeOwnership"] = df["HomeOwnership"].map({"Rent": 1, "Mortgage": 2, "Own": 3})

    print("First 5 records after converting categorical features & labels into numerical format")
    print(df.head())

    seperate_features_and_labels(df)

def perform_eda_on_dataset(df):
    if df.isnull().values.any():
        if df.isnull().sum().sum() > 0:
            print("Dataset has missing values. Cleaning the dataset before proceeding further.")
            df = df.dropna()
    
            print("Dataset cleaned successfully...")
            print(BORDER)
            check_classes_distribution(df)
    else:
        check_classes_distribution(df)

def load_data_set(file_name):
    data_frame = pd.read_csv(file_name)

    if len(data_frame.shape) == 0:
        print("No data found in dataset")
        print(BORDER)
        return
    else:
        print("Shape of Dataset: ", data_frame.shape)
        print(BORDER)

        print("Columns in Dataset")
        for col_name in list(data_frame.columns):
            print(col_name)
        print(BORDER)
        
        print("First 5 records from Dataset to understand the data")
        print(data_frame.head())
        print(BORDER)

        print("Dataset loaded successfully. Proceeding further for exploratory data analysis of dataset")
        print(BORDER)

        perform_eda_on_dataset(data_frame)

def main():
    load_data_set(FILE_NAME)

if __name__ == "__main__":
    main()