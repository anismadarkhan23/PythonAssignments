import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler, LabelEncoder

DATASET_PATH = "MarvellousInfosystems_PlayPredictor.csv"
BORDER = "-" * 50

class PlayPredictMLPipeline:

    def __init__(self, test_size = 0.5, random_state = 42, neighbour_value = 3):
        self.test_size = test_size
        self.random_state = random_state
        self.neighbour_value = neighbour_value
        
        self.X_train = None
        self.X_test = None
        self.Y_train = None
        self.Y_test = None

        self.scaler = StandardScaler()
        self.model = KNeighborsClassifier(neighbour_value)

    # Step 3: Do the scaling & train the whole dataset.
    def scale_and_train_dataset(self, X: pd.DataFrame, Y: pd.Series):
        print("Scaling the dataset...")
        print(BORDER)
                
        self.X_train = self.scaler.fit_transform(X)
        self.X_test = self.scaler.transform(X)

        print("Shape of scaled X train: ", self.X_train.shape)
        print("Shape of scaled x test: ", self.X_test.shape)

        print(BORDER)
        print("Dataset has been scaled successfully")
        print(BORDER)

        self.model.fit(self.X_train, Y)

    # Step 4: Testing the data for randomly passed wether & temperature.
    def test_model_for_random_passed_data(self):
        wether = input("Enter the wether: ")
        if wether not in ["Sunny", "Overcast", "Rainy"]:
            print("Invalid wether input. Please enter 'Sunny', 'Overcast', or 'Rainy'.")
            print(BORDER)
            return

        temp = input("Enter the temperature: ")
        if temp not in ["Hot", "Mild", "Cool"]:
            print("Invalid temperature input. Please enter 'Hot', 'Mild', or 'Cool'.")
            print(BORDER)
            return
    
        test_random_data = {
            "Wether" : [wether],
            "Temperature" : [temp]
        }

        test_random_data = pd.DataFrame(test_random_data)

        test_random_data["Wether"] = test_random_data["Wether"].map({"Sunny": 1, "Overcast": 2, "Rainy": 3})
        test_random_data["Temperature"] = test_random_data["Temperature"].map({"Hot": 11, "Mild": 21, "Cool": 31})

        test_random_data_scaled = self.scaler.transform(test_random_data)

        print(BORDER)
        print("Tested the model & predicted the result")

        predicted_result = self.model.predict(test_random_data_scaled)

        print(BORDER)
        print("Can play: ", predicted_result[0])
        print(BORDER)

    # Step 5: Split the dataset for calculating the accuracy.
    def split_dataset(self, X: pd.DataFrame, Y: pd.Series):
        print("Spliting the dataset for training and testing...")
        print(BORDER)
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(X, 
                                                                                Y, 
                                                                                test_size = self.test_size, 
                                                                                random_state = self.random_state, 
                                                                                stratify = Y)
        print("Details of trainning and testing data")
        print("Shape of X_train: ",  self.X_train.shape)
        print("Shape of X_test: ",  self.X_test.shape)
        print("Shape of Y_train: ",  self.Y_train.shape)
        print("Shape of Y_test: ",  self.Y_test.shape)
        print("Dataset has been splited successfully for trainning & testing")
        print(BORDER)

    # Step 6: Calculate the accuracy
    def build_train_test_the_model(self):
        print("Building the AI model....")
        print("AI model has been built successfully")
        print(BORDER)

        print("Training the AI model")
        self.model.fit(self.X_train, self.Y_train)
        print("AI model has been trained successfully")
        print(BORDER)

        print("Testing the AI model")
        Y_pred = self.model.predict(self.X_test)
        print("AI model has been tested successfully")
        print(BORDER)

        accuracy = accuracy_score(self.Y_test, Y_pred)
        print(f"Model accuracy is: {accuracy * 100:.2f}%")
        print(BORDER)


class PlayPredictorModel(PlayPredictMLPipeline):
    def __init__(self, dataset_path = str, test_size = 0.5):
        super().__init__(test_size = test_size)
        self.dataset_path = dataset_path
        self.data_frame = None
    
    def load_and_do_eda(self):
        print(BORDER)
        self.data_frame = pd.read_csv(self.dataset_path)

        # Step 2: Data manipulation
        self.data_frame["Wether"] = self.data_frame["Wether"].map({"Sunny": 1, "Overcast": 2, "Rainy": 3})
        self.data_frame["Temperature"] = self.data_frame["Temperature"].map({"Hot": 11, "Mild": 21, "Cool": 31})

        print("Dataset manimulated successfully")
        print(BORDER)

        if self.data_frame.isnull().values.any():
            if self.data_frame.isnull().sum().sum() > 0:
                self.data_frame.dropna(inplace = True)

        print("EDA performed on dataset & Dataset has been loaded successfully")
        print(BORDER)

        print("Some records from dataset for reference after performing EDA")
        print(BORDER)

        print(self.data_frame.head())
        print(BORDER)

    def do_ops_on_model(self):
        if self.data_frame is None:
            # Step 1: Load the dataset
            self.load_and_do_eda()

        X = self.data_frame[["Wether", "Temperature"]]
        Y = self.data_frame["Play"]

        # Step 3: Do the scaling & train the whole dataset.
        self.scale_and_train_dataset(X, Y)

        # Step 4: Testing the data for randomly passed wether & temperature.
        self.test_model_for_random_passed_data()

        # Step 5: Split the dataset for calculating the accuracy.
        self.split_dataset(X, Y)

        # Step 6: Calculate the accuracy
        self.build_train_test_the_model()

ppm_obj = PlayPredictorModel(DATASET_PATH)
ppm_obj.do_ops_on_model()
