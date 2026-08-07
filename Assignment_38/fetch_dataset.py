import pandas as pd

DATASET_PATH = "student_performance_ml.csv"
BORDER = "-" * 110

def load_dataset(file_path):
    df = pd.read_csv(file_path)
    return df
