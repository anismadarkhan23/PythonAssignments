from fetch_dataset import load_dataset, DATASET_PATH, BORDER
import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram():

    # Loading the dataset from given path
    df = load_dataset(DATASET_PATH)

    # This will define the plot's size. Here it will be 8 is width & 5 is height
    plt.figure(figsize = (8, 5))
    
    plt.hist(                   # The hist will help you draw the histogram.
        df['StudyHours'],       # The first parameter shows X axis values which is StudyHours data here in case
        color = 'green',        # The color parameter will diplay the histograms's bars in green color
        edgecolor = 'black',    # The edgecolor parameter will display the edge color of bars in black
        alpha = 0.7             # The alpha parameter will controls the transparency (or opacity) of the plot elements
        )

    # This will set the title of histogram
    plt.title("Student Performance Case Study")

    # This will set the label for X-axis of histogram
    plt.xlabel("Study Hours")

    # This will set the label for Y-axis of histogram
    plt.ylabel("Frequency")

    # This will display grid lines inside plot.
    plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)

    # This will display the plot
    plt.show()

def main():
    plot_histogram()

if __name__ == "__main__":
    main()

# Histogram :
# The X-axis shows the range of study hours, 
# while the Y-axis shows the number (frequency) of students in each range.