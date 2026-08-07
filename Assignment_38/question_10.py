from fetch_dataset import load_dataset, DATASET_PATH
import matplotlib.pyplot as plt

def generate_plot_scatter():

    # Loading the dataset from given path
    df = load_dataset(DATASET_PATH)

    # This will define the plot's size. Here it will be 8 is width & 5 is height
    plt.figure(figsize = (7,5))

    plt.plot(               # The plot will help you draw the scatter plot.
        df["SleepHours"],   # The first parameter shows X axis values which is Assignment completed data here in case
        df["FinalResult"],  # The second parameter shows Y axis values which is Final result data here in case
        marker = "o"
        )

    # This will set the title of Scatter plot
    plt.title("Sleep Hours vs Final Result")

    # This will set the label for X-axis of Scatter plot
    plt.xlabel("Sleep Hours")

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

# Explaination of plot diagram (Sleep Hours vs Final Result):
# 1. Sleeping 7 to 8 hours can produce a passing result (1).
# 2. Sleeping only 5 hours leads to a fail (0), 
#    which indicates that due to lack of rest it will negatively impacts the result.
#    then the final result is appeared to be as 0 which means students are failed in final result.
# 3. Sleeping 12 hours also leads to a fail (0), 
#    suggesting excessive sleep is harmful and scientifically it leads to lazyness.
#    which, causes a negative impact on the final result.
# 4. At 6 hours of sleep, there are data points for both 0 (Fail) and 1 (Pass), 
#    showing that 6 hours sits on the edge where individual outcomes vary based on other factors.