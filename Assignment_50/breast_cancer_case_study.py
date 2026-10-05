import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

BORDER = "-" * 150
DATASET_PATH = "breast_cancer.csv"

def predict_breast_cancer(bc_model):
    print("Enter the biological parameters of the tumor to predict whether it is benign or malignant")
    mean_radius = float(input("Mean Radius: "))
    mean_texture = float(input("Mean Texture: "))
    mean_perimeter = float(input("Mean Perimeter: "))
    mean_area = float(input("Mean Area: "))
    mean_smoothness = float(input("Mean Smoothness: "))
    mean_compactness = float(input("Mean Compactness: "))
    mean_concavity = float(input("Mean Concavity: "))
    mean_concave_points = float(input("Mean Concave Points: "))
    mean_symmetry = float(input("Mean Symmetry: "))
    mean_fractal_dimension = float(input("Mean Fractal Dimension: "))
    radius_error = float(input("Radius Error: "))
    texture_error = float(input("Texture Error: "))
    perimeter_error = float(input("Perimeter Error: "))
    area_error = float(input("Area Error: "))
    smoothness_error = float(input("Smoothness Error: "))
    compactness_error = float(input("Compactness Error: "))
    concavity_error = float(input("Concavity Error: "))
    concave_points_error = float(input("Concave Points Error: "))
    symmetry_error = float(input("Symmetry Error: "))
    fractal_dimension_error = float(input("Fractal Dimension Error: "))
    worst_radius = float(input("Worst Radius: "))
    worst_texture = float(input("Worst Texture: "))
    worst_perimeter = float(input("Worst Perimeter: "))
    worst_area = float(input("Worst Area: "))
    worst_smoothness = float(input("Worst Smoothness: "))
    worst_compactness = float(input("Worst Compactness: "))
    worst_concavity = float(input("Worst Concavity: "))
    worst_concave_points = float(input("Worst Concave Points: "))
    worst_symmetry = float(input("Worst Symmetry: "))
    worst_fractal_dimension = float(input("Worst Fractal Dimension: "))

    tumor_data = pd.DataFrame([{
        "mean_radius": mean_radius,
        "mean_texture": mean_texture,
        "mean_perimeter": mean_perimeter,
        "mean_area": mean_area,
        "mean_smoothness": mean_smoothness,
        "mean_compactness": mean_compactness,
        "mean_concavity": mean_concavity,
        "mean_concave_points": mean_concave_points,
        "mean_symmetry": mean_symmetry,
        "mean_fractal_dimension": mean_fractal_dimension,
        "radius_error": radius_error,
        "texture_error": texture_error,
        "perimeter_error": perimeter_error,
        "area_error": area_error,
        "smoothness_error": smoothness_error,
        "compactness_error": compactness_error,
        "concavity_error": concavity_error,
        "concave_points_error": concave_points_error,
        "symmetry_error": symmetry_error,
        "fractal_dimension_error": fractal_dimension_error,
        "worst_radius": worst_radius,
        "worst_texture": worst_texture,
        "worst_perimeter": worst_perimeter,
        "worst_area": worst_area,
        "worst_smoothness": worst_smoothness,
        "worst_compactness": worst_compactness,
        "worst_concavity": worst_concavity,
        "worst_concave_points": worst_concave_points,
        "worst_symmetry": worst_symmetry,
        "worst_fractal_dimension": worst_fractal_dimension
    }])

    scaler = StandardScaler()
    tumor_data = scaler.fit_transform(tumor_data)

    result = bc_model.predict(tumor_data)

    if result[0] == 0:
        print("The tumor is predicted to be benign i.e. non-cancerous.")
    else:
        print("The tumor is predicted to be malignant i.e. cancerous.")
    
def evaluate_model(bc_model, model_predicted_result, Y_labels_test):
    model_accuracy = accuracy_score(Y_labels_test, model_predicted_result)
    print(f"Overall Model Accuracy : {model_accuracy * 100:.2f}%")
    print(BORDER)

    cm = confusion_matrix(Y_labels_test, model_predicted_result)
    print("Confusion Matrix")
    print(cm)
    print(BORDER)

    ps = precision_score(Y_labels_test, model_predicted_result)
    print(f"Precision Score : {ps * 100:.2f}%")
    print(BORDER)

    rs = recall_score(Y_labels_test, model_predicted_result)
    print(f"Recall Score : {rs * 100:.2f}%")
    print(BORDER)

    f1s = f1_score(Y_labels_test, model_predicted_result)
    print(f"F1 Score : {f1s * 100:.2f}%")
    print(BORDER)

    predict_breast_cancer(bc_model)

def test_model(bc_model, X_features_test, Y_labels_test):
    model_predicted_result = bc_model.predict(X_features_test)

    print("Model testing completed successfully...")
    print(BORDER)

    evaluate_model(bc_model, model_predicted_result, Y_labels_test)

def scale_and_train_model(X_features_train, 
                X_features_test, 
                Y_labels_train, 
                Y_labels_test):
    
    scaler = StandardScaler()
    bc_model = LogisticRegression()

    X_features_train = scaler.fit_transform(X_features_train)
    X_features_test = scaler.transform(X_features_test)
    
    print("Features scaled successfully...")
    print(BORDER)

    bc_model.fit(X_features_train, Y_labels_train)

    print("Model trained successfully...")
    print(BORDER)

    test_model(bc_model, X_features_test, Y_labels_test)

def split_train_test_model(features, labels):
    X_train, X_test, Y_train, Y_test = train_test_split(features, labels, test_size = 0.5, random_state = 42)
        
    print("Dataset splitted for building, traning & testing the model...")
    print(BORDER)

    scale_and_train_model(X_train, X_test, Y_train, Y_test)

def get_features_and_labels(df):
    print("Generating independent and dependent data....")
    print(BORDER)

    features_columns = df.drop("target", axis = 1)
    label_column = df["target"]

    print("Independent features columns: ")
    for col_name in list(features_columns.columns):
        print(col_name)
    print(BORDER)

    print("Dependent label column: ", label_column.name)
    print(BORDER)

    return features_columns, label_column

def perform_operations_to_prepare_model(df):
    features, labels = get_features_and_labels(df)
    
    split_train_test_model(features, labels) 

def check_classes_distribution(df):
    print("Checking the distribution of classes in the dataset")
    print(BORDER)
    print(df["target"].value_counts())
    print(BORDER)

    perform_operations_to_prepare_model(df)

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

def load_data():
    data_frame = pd.read_csv(DATASET_PATH)

    if len(data_frame.shape) == 0:
        print("No data found in dataset")
        print(BORDER)
        return
    else:
        print("First 10 records from Dataset to understand the data")
        print(data_frame.head(10))
        print(BORDER)

        print("Shape of Dataset: ", data_frame.shape)
        print(BORDER)

        print("Dataset loaded successfully. Proceeding further for exploratory data analysis of dataset")
        print(BORDER)

        perform_eda_on_dataset(data_frame)
    
def perform_ml_ops():
    if not os.path.exists(DATASET_PATH):
        print(f"Dataset file '{DATASET_PATH}' not found.")
        print(BORDER)
        return
    else:
        print("Dataset file path exists at mentioned location.")
        print(BORDER)
        load_data()

def main():
    perform_ml_ops()

if __name__ == "__main__":
    main()