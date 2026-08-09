import os
import sys
import pandas as pd
from getvisualisationdiagrams import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

DATASET_PATH = "WinePredictor.csv"
BORDER = "-" * 100

def check_model_accuracy(wp_model, model_predicted_result, 
                         X_features_train, X_features_test, 
                         Y_labels_train, Y_labels_test):

    train_accuracy = wp_model.score(X_features_train, Y_labels_train)
    print("Model Training Accuracy : ", train_accuracy * 100, "%")
    print(BORDER)

    test_accuracy = wp_model.score(X_features_test, Y_labels_test)
    print("Model Testing Accuracy : ", test_accuracy * 100, "%")
    print(BORDER)

    model_accuracy = accuracy_score(Y_labels_test, model_predicted_result)
    print("Overall Model Accuracy : ", model_accuracy * 100, "%")
    print(BORDER)

    design_plot_tree(wp_model, X_features_train.columns)

def test_model(wp_model, 
               X_features_train, 
               X_features_test, 
               Y_labels_train, 
               Y_labels_test):

    model_predicted_result = wp_model.predict(X_features_test)

    print("Model testing completed successfully...")
    print(BORDER)

    check_model_accuracy(wp_model, model_predicted_result, 
                         X_features_train, X_features_test, 
                         Y_labels_train, Y_labels_test)

def train_model(X_features_train, 
                X_features_test, 
                Y_labels_train, 
                Y_labels_test):

    wp_model = DecisionTreeClassifier(max_depth = 5)

    wp_model.fit(X_features_train, Y_labels_train)

    print("Model trained successfully...")
    print(BORDER)

    test_model(wp_model, X_features_train, X_features_test, Y_labels_train, Y_labels_test)

def get_features_and_labels(df):
    print("Generating independent and dependent data....")

    features_columns = df.drop("Class", axis = 1)
    label_column = df["Class"]

    return features_columns, label_column

def split_train_test_model(X_features, Y_labels):
    X_train, X_test, Y_train, Y_test = train_test_split(X_features, Y_labels, 
                                                            test_size = 0.5, random_state = 42)
        
    print("Dataset splitted for building, traning & testing the model...")
    print(BORDER)

    train_model(X_train, X_test, Y_train, Y_test)

def perform_ops_to_prepare_model(df):
    X_features, Y_labels = get_features_and_labels(df)

    split_train_test_model(X_features, Y_labels)

def visualise_wine_dataset(df):
    boxplot_wineprediction_dataset(df)
    scatterplot_wineprediction_dataset(df)

    perform_ops_to_prepare_model(df)

def check_classes_distribution(df):
    print("Checking classes distribution from features & labels of dataset")
    print(BORDER)

    print("Class distribution of Wine Class:")
    print(BORDER)
    print(df["Class"].value_counts())
    print(BORDER)
    
    visualise_wine_dataset(df)

def perform_eda_on_dataset(df):
    if df.isnull().values.any():
        if df.isnull().sum().sum() > 0:
            print("Dataset has missing values. Cleaning the dataset before proceeding further.")
            df = df.dropna()
    
            print("Dataset cleaned successfully...")
            print(BORDER)
    else:
        check_classes_distribution(df)

def load_winepredictor_dateset():
    data_frame = pd.read_csv(DATASET_PATH)

    if len(data_frame.shape) == 0:
        print("No data found in dataset")
        print(BORDER)
        return
    else:
        print("Dataset loaded successfully. Proceeding further for exploratory data analysis of dataset")
        print(BORDER)
        perform_eda_on_dataset(data_frame)

def main():
    if not os.path.exists(DATASET_PATH):
        print("Dataset file not found. Please, provide correct path.")
        print(BORDER)
    else:
        print(f"Dataset file path exists at location.")
        print(BORDER)
        load_winepredictor_dateset()

if __name__ == "__main__":
    main()

