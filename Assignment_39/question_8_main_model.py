# Importing required libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# Importing required libraries

# Global variables & Expressions
DATASET_PATH = "student_performance_ml.csv"
BORDER = "-" * 110
# Global variables & Expressions

# Step 14 Start -> Function to generate the classification report for the model's predictions.
def generate_classification_report(model_predicted_result, Y_resultType_test):

    # Generating the classification report for the model's predictions.
    print("Classification Report")
    print(classification_report(Y_resultType_test, model_predicted_result))
    print(BORDER)
# End

# Step 13 Start -> Function to display the confusion matrix for the model's predictions.
def display_confusion_matrix(model_predicted_result, Y_resultType_test):

    # Calculating the confusion matrix for the model's predictions.
    print("Confusion Matrix")
    print(confusion_matrix(Y_resultType_test, model_predicted_result))

    print(BORDER)  

    # Calling the function to generate the classification report for the model's predictions.
    generate_classification_report(model_predicted_result, Y_resultType_test)  
# End

# Step 12 Start -> Function to check the accuracy of the model.
def check_model_accuracy(sp_model, model_predicted_result, 
                         X_studyParams_train, X_studyParams_test, 
                         Y_resultType_train, Y_resultType_test):

    # Calculating the training accuracy of the model using the training data.
    train_accuracy = sp_model.score(X_studyParams_train, Y_resultType_train)
    print("Model Training Accuracy : ", train_accuracy * 100, "%")
    print(BORDER)

    # Calculating the testing accuracy of the model using the testing data.
    test_accuracy = sp_model.score(X_studyParams_test, Y_resultType_test)
    print("Model Testing Accuracy : ", test_accuracy * 100, "%")
    print(BORDER)

    # Calculating the overall accuracy of the model using the testing data.
    model_accuracy = accuracy_score(Y_resultType_test, model_predicted_result)
    print("Overall Model Accuracy : ", model_accuracy * 100, "%")
    print(BORDER)

    # Calling the function to display the confusion matrix for the model's predictions.
    display_confusion_matrix(model_predicted_result, Y_resultType_test)
# End

# Step 11 Start -> Function to test the model.
def test_model(sp_model, 
               X_perfParams_train, 
               X_perfParams_test, 
               Y_resultType_train, 
               Y_resultType_test):

    # Using the trained model to predict the results for the testing data.
    model_predicted_result = sp_model.predict(X_perfParams_test)

    print("Model testing completed successfully...")
    print(BORDER)

    # Calling the function to check the model accuracy using the training and testing data.
    check_model_accuracy(sp_model, model_predicted_result, 
                         X_perfParams_train, X_perfParams_test, 
                         Y_resultType_train, Y_resultType_test)
# End

# Step 10 Start -> Function to train the model.
def train_model(X_perfParams_train, 
                X_perfParams_test, 
                Y_resultType_train, 
                Y_resultType_test):

    # Creating an instance of DecisionTreeClassifier with a maximum depth of 3.
    # The max_depth parameter limits the depth of the tree to prevent overfitting.
    # The DecisionTreeClassifier is a machine learning model that can be used for classification tasks.
    # Overfitting means if trainning accuracy is very high & testing accuracy is low 
    # which means model fails on unseen data.
    sp_model = DecisionTreeClassifier(max_depth = 3)

    # Fitting the model to the training data using the fit() method.
    sp_model.fit(X_perfParams_train, Y_resultType_train)

    print("Model trained successfully...")
    print(BORDER)

    # Calling the function to test the model using the testing data and evaluate its performance.
    test_model(sp_model, X_perfParams_train, X_perfParams_test, Y_resultType_train, Y_resultType_test)
# End

# Step 8 Start -> Function to get the independent and dependent data from the dataset.
def get_independent_dependent_data(df):
    print("Generating independent and dependent data....")

    # Defining the independent columns which will be used to 
    # predict the dependent column "FinalResult"
    independent_columns = [
        "StudyHours", 
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
        ]

    # Creating a new DataFrame 'perf_parameters' that contains only the 
    # independent columns from the original DataFrame 'df'.
    perf_parameters = df[independent_columns]

    # Creating a new Series 'result_type' that contains the dependent 
    # column "FinalResult" from the original DataFrame 'df'.
    result_type = df["FinalResult"]

    print("Independent and dependent data generated successfully...")
    print(BORDER)

    # Returning the independent and dependent data for further processing.
    return perf_parameters, result_type
# End

# Step 9 Start -> Function to split the dataset into training and testing sets 
# for building, training & testing the model.
def split_train_test_model(perfParams, resultType):

    # 1. Splitting the dataset into training and testing sets 
    # using train_test_split function from sklearn.
    # 2. The test_size parameter specifies the proportion of the 
    # dataset to include in the test split (0.5 means 50% for testing).
    # 3. The random_state parameter is used for initializing the internal random 
    # number generator, which will decide the splitting of data into train and test indices.
    X_train, X_test, Y_train, Y_test = train_test_split(perfParams, resultType, 
                                                        test_size = 0.5, random_state = 42)
    
    print("Dataset splitted for building, traning & testing the model...")
    print(BORDER)

    # Calling the function to train the model using the training and testing data.
    train_model(X_train, X_test, Y_train, Y_test)
# End

# Step 7 Start -> Function to prepare the dataset for building, training & testing the model.
def do_ops_for_model_prep(df):

    # Calling the function to get the independent and dependent data from the dataset.
    X_perfParams, Y_resultType = get_independent_dependent_data(df)

    # Calling the function to split the dataset into training and testing 
    # sets for building, training & testing the model.
    split_train_test_model(X_perfParams, Y_resultType)
# End

# Step 6 Start -> Function to visualise the dataset using scatter plot.
def visualise_the_dataset(df):

    # .figure() function is used to set the figure size for the plot. 
    # The figsize parameter takes a tuple of two values, 
    # which represent the width and height of the figure in inches.
    plt.figure(figsize = (8, 5))

    # Iterating over every unique category/label in the "FinalResult" column. 
    # Here, it will be 0(Fail) & 1(Pass) 
    for sp in df["FinalResult"].unique():

        # Filtering the main DataFrame 'df' to extract only the rows where 
        # the "FinalResult" matches the current category 'sp', and store them in 'temp'        
        temp = df[df["FinalResult"] == sp]
        plt.scatter(                                        # The scatter will help you draw the scatter plot.
                    temp["StudyHours"],                     # The first parameter shows X axis values which is StudyHours data here in case
                    temp["PreviousScore"],                  # The second parameter shows Y axis values which is PreviousScore data here in case
                    label = "Pass" if sp == 1 else "Fail",  # The label parameter will diplay the Pass & Fail.
                    color = "green" if sp == 1 else "red",  # The color parameter will display the green color for Pass students & Red for Fail students.
                    s = 50                                  # The s parameter will display the size of dots which depicts the data.
                    )

    # This will set the title of scatter plot. 
    # Here it will be "Student Performance Case Study"
    plt.title("Student Performance Case Study")

    # This will set the label for X-axis of scatter plot.
    plt.xlabel("Study Hours")

    # This will set the label for Y-axis of scatter plot.
    plt.ylabel("Previous Score")

    # This will read the labels passed which are passed in .scatter method 
    # and diplay the visual key box
    plt.legend()

    # This will display grid lines inside plot.
    plt.grid()

    # This will display the scatter plot.
    plt.show()

    print("Model visualisation using mathmatical graph representation displayed successfully...")
    print(BORDER)

    # Calling the function to prepare the dataset for building, training & testing the model.
    do_ops_for_model_prep(df)
# End

# Step 5 Start -> Function to check the class distribution in the dataset.                   
def check_class_distribution(df):
    print("Checking class distribution...")
    print("Class distribution (FinalResult)")

    # Checking the class distribution in the dataset.
    print(df["FinalResult"].value_counts())

    print(BORDER)

    # Calling the function to visualise the dataset using scatter plot.
    visualise_the_dataset(df)
# End

# Step 4 Start -> Function to do the data analysis on the dataset.
def do_data_analysis(df):

    print(BORDER)
    print("Checking missing values per column...")

    # This if conditionline will check the missing values per column in the dataset.
    if not df.isnull().values.any():
        print("Dataset has no missing values. Proceeding further...")
        print(BORDER)

    # This elif conditionline will check if the dataset has any missing values.
    elif df.isnull().sum().sum() > 0:
        print("Dataset has missing values. Cleaning the dataset before proceeding further...")

        # This line will drop the rows with missing values from the dataset.
        df = df.dropna()

        print("Dataset cleaned successfully...")
        print(BORDER)

    # Calling the function to check the class distribution in the dataset.
    check_class_distribution(df)
# End

# Step 3 Start -> Function to load the dataset from the given file path.
def load_dataset(file_path):

    # Reading the dataset from the given file path and do the data analysis.
    data_frame = pd.read_csv(file_path)
    print(f"Dataset loaded successfully from path {os.path.abspath(file_path)}")

    # Calling the function to do the data analysis on the dataset.
    do_data_analysis(data_frame)
# End

# Step 2 Start -> Entry point of the script
def main():

    # Checking if dataset file exists at the given path
    if not os.path.exists(DATASET_PATH):
        print("Dataset file not found at path: ", DATASET_PATH)
        print(BORDER)
    else:
        # Loading the dataset.
        load_dataset(DATASET_PATH)
# End

# Step 1 Start -> Starter of the script
if __name__ == "__main__":
    main()
# End
