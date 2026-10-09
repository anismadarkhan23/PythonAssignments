import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

BORDER = "-" * 75

def predict_customer_service_feedback():
    data_set = ({
        "Age": [25, 30, 45, 50, 28, 35, 48, 52, 27, 42],
        "Monthly_Charges": [500, 700, 1200, 1500, 600, 800, 1400, 1600, 550, 1300],
        "Tenure": [12, 24, 6, 5, 18, 30, 4, 3, 20, 8],
        "Complaints":[1, 0, 5, 6, 1, 0, 7, 8, 0, 4],
        "Support_Calls":[2, 1, 8, 10, 1, 0, 9, 12, 1, 7],
        "FeedbackStatus":[0, 0, 1, 1, 0, 0, 1, 1, 0, 1]
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
    print(df["FeedbackStatus"].value_counts())
    print(BORDER)

    X_features = df.drop("FeedbackStatus", axis = 1)
    Y_label = df["FeedbackStatus"]

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

    print("Enter new customer details to predict whether the customer will stay or leave")
    age = int(input("Enter the customer's age: "))
    monthly_charges = int(input("Enter the monthly charges accured to customer: "))
    tenure = int(input("Enter the tenure: "))
    complaints = int(input("Enter the total number of complaints raised by customer: "))
    support_calls = int(input("Enter the number of support calls customer received: "))

    new_customer = pd.DataFrame([{
        "Age": age,
        "Monthly_Charges": monthly_charges,
        "Tenure": tenure,
        "Complaints": complaints,
        "Support_Calls": support_calls
    }])

    scaled_new_customer = scaler.transform(new_customer)

    predictions = model.predict(scaled_new_customer)
    new_customer["FeedbackStatus"] = pd.Series(predictions).map({1: "Leave", 0: "Stay"})

    print("Attrition predictions for the entered employees")
    print(new_customer.to_string(index=False))
    print(BORDER)

def main():
    predict_customer_service_feedback()

if __name__ == "__main__":
    main()