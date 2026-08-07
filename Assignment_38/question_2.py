from fetch_dataset import load_dataset, DATASET_PATH, BORDER

def display_student_raw_information(file_path):
    data_frame = load_dataset(file_path)
    print(BORDER)
    print(f"Total number of students are {len(data_frame.index)}")

    print(BORDER)
    passed_student = list(filter(lambda x: x == 1, data_frame["FinalResult"]))
    failed_student = list(filter(lambda x: x == 0, data_frame["FinalResult"]))
    print(f"Total passed students are {len(passed_student)}")
    print(f"Total failed students are {len(failed_student)}")
    print(BORDER)

def main():
    display_student_raw_information(DATASET_PATH)

if __name__ == "__main__":
    main()