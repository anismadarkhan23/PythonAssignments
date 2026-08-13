import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

DATASET_PATH = "WinePredictor.csv"
BORDER = "-" * 50

class AIModelKNNClassifier:

    def __init__(self, test_size = 0.5, random_state = 42, neighbour_value = 9):
        self.test_size = test_size
        self.random_state = random_state
        self.neighbour_value = neighbour_value
        
        self.X_train = None
        self.X_test = None
        self.Y_train = None
        self.Y_test = None

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

    def scale_the_dataset(self):
        print("Scaling the dataset...")
        print(BORDER)
                
        scaler = StandardScaler()
        self.X_train = scaler.fit_transform(self.X_train)
        self.X_test = scaler.transform(self.X_test)

        print("Shape of scaled X train: ", self.X_train.shape)
        print("Shape of scaled x test: ", self.X_test.shape)
        print("Dataset has been scaled successfully")

        print(BORDER)

    def build_train_test_the_model(self):
        print("Building the AI model....")
        model = KNeighborsClassifier(n_neighbors = self.neighbour_value)
        print("AI model has been built successfully")
        print(BORDER)

        print("Training the AI model")
        model = model.fit(self.X_train, self.Y_train)
        print("AI model has been trained successfully")
        print(BORDER)

        print("Testing the AI model")
        Y_pred = model.predict(self.X_test)
        print("AI model has been tested successfully")
        print(BORDER)

        accuracy = accuracy_score(self.Y_test, Y_pred)
        print(f"Model accuracy is: {accuracy * 100:.2f}%")
        print(BORDER)

class KNNClassifier(AIModelKNNClassifier):

    def __init__(self, dataset_path = str, test_size = 0.5):
        super().__init__(test_size = test_size)

        self.dataset_path = dataset_path
        self.data_frame = None
    
    def load_and_do_eda(self):
        print(BORDER)
        self.data_frame = pd.read_csv(self.dataset_path)

        if self.data_frame.isnull().values.any():
            if self.data_frame.isnull().sum().sum() > 0:
                self.data_frame.dropna(inplace = True)
                print("EDA performed on dataset successfully")

        print("Shape of dataset: ", self.data_frame.shape)
        print("Total records: ", self.data_frame.shape[0])
        print("Total columns: ", self.data_frame.shape[1])
        print(BORDER)

        print("Some records from dataset for reference after performing EDA")
        print(self.data_frame.head())
        print(BORDER)

    def do_ops_on_model(self):
        if self.data_frame is None:
            self.load_and_do_eda()

        X = self.data_frame.drop(columns = ["Class"])
        Y = self.data_frame["Class"]

        self.split_dataset(X, Y)
        self.scale_the_dataset()
        self.build_train_test_the_model()

knn_object = KNNClassifier(DATASET_PATH)
knn_object.do_ops_on_model()