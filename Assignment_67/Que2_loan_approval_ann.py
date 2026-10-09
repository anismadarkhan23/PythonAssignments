import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

BORDER = "-" * 75

def predict_customer_loan_approval_status():
    data_set = ({
        "Income": [25000, 40000, 60000, 20000, 80000, 35000, 18000, 90000, 30000, 70000],
        "CreditScore": [600, 700, 750, 550, 800, 650, 500, 850, 580, 780],
        "LoanAmount": [200000, 300000, 500000, 150000, 700000, 250000, 100000, 800000, 200000, 600000],
        "ExistingEMI":[10000, 8000, 12000, 15000, 10000, 9000, 12000, 15000, 14000, 10000],
        "EmploymentStatus":["Not Stable", "Stable", "Stable", "Not Stable", "Stable", "Stable", "Not Stable", "Stable", "Not Stable", "Stable"],
        "LoanStatus": ["Rejected", "Approved", "Approved", "Rejected", "Approved", "Approved", "Rejected", "Approved", "Rejected", "Approved"]
    })

    df = pd.DataFrame(data_set)

    print(BORDER)
    print("Data set created successfully")
    print(BORDER)

    print("Shape of Dataset: ", df.shape)
    print(BORDER)

    print("Read all records from the data set")
    print(df.head(10))
    print(BORDER)

    if df.isnull().values.any():
        if df.isnull().sum().sum() > 0:
            print("Dataset has missing values. Cleaning the dataset before proceeding further.")
            df = df.dropna()
    
            print("Dataset cleaned successfully...")
            print(BORDER)

    print("Checking the distribution of classes in the dataset")
        
    print(BORDER)
    print(df["LoanStatus"].value_counts())
    print(BORDER)

    df["EmploymentStatus"] = df["EmploymentStatus"].map({"Stable": 1, "Not Stable": 0})
    df["LoanStatus"] = df["LoanStatus"].map({"Approved": 1, "Rejected": 0})
    
    print("First 5 records after converting categorical features & labels into numerical format")
    print(df.head())

    X_features = df.drop("LoanStatus", axis = 1)
    Y_label = df["LoanStatus"]

    print(BORDER)
    print("Input Features are")
    print(X_features.head())

    print(BORDER)
    print("Target Label is")
    print(Y_label.head())
    print(BORDER)

    X_train, X_test, Y_train, Y_test = train_test_split(X_features, Y_label, train_size = 0.9, random_state = 42)
    
    print("Training Input's Shape: ", X_train.shape)
    print(BORDER)

    print("Testing Input's Shape: ", X_test.shape)
    print(BORDER)

    print("Training Output's Shape: ", Y_train.shape)
    print(BORDER)

    print("Testing Output's Shape: ", Y_test.shape)
    print(BORDER)

    scaler = StandardScaler()
    
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("Feature scaling performed on dataset successfully...")
    print(BORDER)

    print("Scaled Training Data")
    print(X_train_scaled[:3])
    print(BORDER)

    print("Scaled Testing Data")
    print(X_test_scaled[:3])
    print(BORDER)

    model = MLPClassifier(
        hidden_layer_sizes = (6, 3),
        activation = 'logistic',
        solver = 'adam',
        max_iter = 500,
        random_state = 42   
    )

    print("FNN Model gets created")
    print(model)
    print(BORDER)

    print("Train the model")
    model.fit(X_train_scaled, Y_train)
    print("Model trainning completed")
    print(BORDER)

    predicted_result = model.predict(X_test_scaled)
    
    model_training_accuracy = model.score(X_train_scaled, Y_train)
    print(f"Model training accuracy is: {model_training_accuracy * 100:.2f}%")
    print(BORDER)

    model_overall_accuracy = accuracy_score(Y_test, predicted_result)
    print(f"Model overall accuracy is: {model_overall_accuracy * 100:.2f}%")
    print(BORDER)

    print("Enter new applicant details to predict whether the loan is Approved or Rejected")
    income = int(input("Enter the applicant's income: "))
    credit_score = int(input("Enter the applicant's credit score: "))
    loan_amount = int(input("Enter the applicant's requested loan amount: "))
    existing_emi_amount = int(input("Enter the applicant's existing EMI amount: "))
    employment_status_response = input("Enter the applicant's current employment status (Stable / Not Stable): ").strip().lower()
    if employment_status_response not in {"stable", "not stable"}:
        raise ValueError("Employment status must be entered as Stable or Not Stable")
    employment_status = 1 if employment_status_response == "stable" else 0

    new_applicant = pd.DataFrame([{
        "Income": income,
        "CreditScore": credit_score,
        "LoanAmount": loan_amount,
        "ExistingEMI": existing_emi_amount,
        "EmploymentStatus": employment_status
    }])

    scaled_new_applicant = scaler.transform(new_applicant)

    predictions = model.predict(scaled_new_applicant)
    new_applicant["LoanStatus"] = pd.Series(predictions).map({1: "Approved", 0: "Rejected"})

    print("Attrition predictions for the entered employees")
    print(new_applicant.to_string(index=False))
    print(BORDER)

def main():
    predict_customer_loan_approval_status()

if __name__ == "__main__":
    main()