from fetch_dataset import load_dataset, DATASET_PATH
import matplotlib.pyplot as plt

def generate_plot_scatter():

    # Loading the dataset from given path
    df = load_dataset(DATASET_PATH)

    # This will define the plot's size. Here it will be 8 is width & 5 is height
    plt.figure(figsize = (7,5))

    plt.plot(                       # The plot will help you draw the scatter plot.
        df["AssignmentsCompleted"], # The first parameter shows X axis values which is Assignment completed data here in case
        df["FinalResult"],          # The second parameter shows Y axis values which is Final result data here in case
        marker = "o"
        )

    # This will set the title of Scatter plot
    plt.title("Assignments Completed vs Final Result")

    # This will set the label for X-axis of Scatter plot
    plt.xlabel("Assignments Completed")

    # This will set the label for Y-axis of Scatter plot
    plt.ylabel("Final Result")

    # This will display grid lines inside plot.
    plt.grid()

    # This will display the plot
    plt.show()

def main():
    generate_plot_scatter()

if __name__ == "__main__":
    main()

# Explaination of plot diagram (Assignments Completed vs Final Result):
# 1. The plot visualizes the relationship between the number 
#    of assignments(X-axis) completed by students and their final results(Y-axis).
# 2. If assignments completed count lies between 0 to 5 on X-axis,
#    then the final result is appeared to be as 0 which means students are failed in final result.
# 3. If assignments completed count lies between 6 to 10 on X-axis,
#    then the final result is appeared to be as 1 which means students are passed in final result.
# 4. We can say that, if students are completing the exactly 5 assignments appears to be the 
#    borderline case where students can either pass or fail in final result which can depends on
#    other dataset's factors.
