from fetch_dataset import load_dataset, DATASET_PATH, BORDER
from tabulate import tabulate

def display_dataset_information(file_path):
    data_frame = load_dataset(file_path)
    print(BORDER)
    print("First 5 records of the student performance dataset is as below.")
    print(tabulate(data_frame.head(), headers = data_frame.columns, tablefmt = "grid"))

    print(BORDER)
    print("Last 5 records of the student performance dataset is as below.")
    print(tabulate(data_frame.tail(), headers = data_frame.columns, tablefmt = "grid"))

    print(BORDER)
    print(f"Total number of rows are {len(data_frame.index)}")
    print(f"Total number of columns are {len(data_frame.columns)}")

    print(BORDER)
    print("List of column names are as below")
    print(list(data_frame.columns))

    print(BORDER)
    print("Data type of each column names are as below")
    print(f"{data_frame.dtypes}")
    print(BORDER)

def main():
    display_dataset_information(DATASET_PATH)

if __name__ == "__main__":
    main()