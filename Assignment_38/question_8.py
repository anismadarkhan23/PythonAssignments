from fetch_dataset import load_dataset, DATASET_PATH
import matplotlib.pyplot as plt

def draw_boxplot():

    # Loading the dataset from given path
    df = load_dataset(DATASET_PATH)

    # This will define the plot's size. Here it will be 7 is width & 5 is height
    plt.figure(figsize = (8, 5))

    plt.boxplot(                               # The boxplot will help you draw the Box plot.
        df["Attendance"],                      # The first parameter shows X axis values which is Attendance data here in case.
        patch_artist = True,                   # Enables filling the inside of the box with color (allows 'facecolor' styling)
        boxprops = dict(facecolor="lightblue") # Passes a dictionary of style properties to set the box's inner color to light blue
        )

    # This will set the title of Box-plot
    plt.title("Attendance of Students")

    # This will set the label for Y-axis of Box-plot
    plt.ylabel("Attendance in percentage")

    # This will display the plot
    plt.show()

def main():
    draw_boxplot()

if __name__ == "__main__":
    main()

# Box-Plot Explaination : 
# The Orange Line (Middle / Median): Lies right at 80%. 
# This means half of the students have attendance above 80%, and half have attendance below 80%.
# The Box Bounds: The box stretches from 70% to 89%. 
# This represents the middle half of the class—most students fall somewhere in this range.
# Top Whisker (Highest Normal Attendance): Reaches up to 96%.
# Bottom Whisker (Lowest Normal Attendance): Drops down to 60%.
# Overall Normal Range: Except for one extreme case, 
# every student in the class has an attendance percentage between 60% and 96%.
# The Single Dot at ~12%: There is a solitary dot way down near 12%. This is an Outlier.