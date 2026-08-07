from fetch_dataset import load_dataset, DATASET_PATH, BORDER

def display_stasticals_details_of_data_set():
    df = load_dataset(DATASET_PATH)

    ave_studyHours = df["StudyHours"].mean()
    ave_attendance = df["Attendance"].mean()
    max_previousScore = df["PreviousScore"].max()
    min_sleepHours = df["SleepHours"].min()

    return ave_studyHours, ave_attendance, max_previousScore, min_sleepHours
    # print(f"Minimum of Sleep Hours is {df["SleepHours"].min()}")

def main():
    average_of_study_hours, average_of_attendance, max_of_previous_score, min_of_sleep_hours = display_stasticals_details_of_data_set()

    print(BORDER)
    print(f"Average of Study Hours is: {average_of_study_hours:.2f}")
    print(BORDER)
    print(f"Average of Attendance is: {average_of_attendance:.2f}")
    print(BORDER)
    print(f"Maximum of Previous Score is: {max_of_previous_score}")
    print(BORDER)
    print(f"Minimum of Sleep Hours is: {min_of_sleep_hours}")
    print(BORDER)

if __name__ == "__main__":
    main()