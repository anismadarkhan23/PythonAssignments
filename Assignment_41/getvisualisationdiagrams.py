import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import plot_tree

def boxplot_wineprediction_dataset(df):
    sns.boxplot(
        x = "Class", 
        y = "Alcohol", 
        data = df
    )

    plt.title("Boxplot for Alcohol by Class in Wine Prediction")
    plt.show()

def scatterplot_wineprediction_dataset(df):
    plt.figure(figsize = (10, 5))
    
    for color_intensity in df["Class"].unique():
        wine_data = df[df["Class"] == color_intensity]

        plt.scatter(                                
            wine_data["Alcohol"],                     
            wine_data["Proline"],                  
            s = 40                                 
            )

    plt.title("Wine Prediction Case Study")
    plt.xlabel("Alcohol")
    plt.ylabel("Malic Acid")
    plt.grid()
    plt.show()

def design_plot_tree(wp_model, X_features_train):
    plt.figure(figsize = (12, 8))
    
    plot_tree(
        wp_model, 
        filled = True, 
        feature_names = X_features_train, 
        rounded = True
    )

    plt.title("Wine Predictor Decision Tree Classifier")
    plt.show()