from fetch_dataset import load_dataset, DATASET_PATH, BORDER
import matplotlib.pyplot as plt

def generate_plot_scatter():

    # Loading the dataset from given path
    df = load_dataset(DATASET_PATH)

    # This will define the plot's size. Here it will be 8 is width & 5 is height
    plt.figure(figsize = (7,5))

    # Iterating over every unique category/label in the "FinalResult" column. 
    # Here, it will be 0(Fail) & 1(Pass) 
    for sp in df["FinalResult"].unique():
        # Filtering the main DataFrame 'df' to extract only the rows where 
        # the "FinalResult" matches the current category 'sp', and store them in 'temp'
        temp = df[df["FinalResult"] == sp]
        
        plt.scatter(                                # The scatter will help you draw the scatter plot.
            temp["StudyHours"],                     # The first parameter shows X axis values which is StudyHours data here in case
            temp["PreviousScore"],                  # The second parameter shows Y axis values which is PreviousScore data here in case
            label = "Pass" if sp == 1 else "Fail",  # The label parameter will diplay the Pass & Fail.
            color = "green" if sp == 1 else "red",  # The color parameter will display the green color for Pass students & Red for Fail students.
            s = 50                                  # The s parameter will display the size of dots which depicts the data.
            )

    # This will set the title of Scatter plot
    plt.title("Student Performance Case Study")

    # This will set the label for X-axis of Scatter plot
    plt.xlabel("StudyHours")

    # This will set the label for Y-axis of Scatter plot
    plt.ylabel("PreviousScore")

    # This will read the labels passed which are passed in .scatter method and diplay the visual key box
    plt.legend()

    # This will display grid lines inside plot.
    plt.grid()

    # This will display the plot
    plt.show()

def main():
    generate_plot_scatter()

if __name__ == "__main__":
    main()