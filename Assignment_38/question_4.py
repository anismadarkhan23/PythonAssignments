from fetch_dataset import load_dataset, DATASET_PATH, BORDER

def analyse_dist_of_finalResult():
    df = load_dataset(DATASET_PATH)

    print(BORDER)
    print("Distribution of column FinalResult")
    print(df["FinalResult"].value_counts())
    print(BORDER)
    print("Percentage of Passed students")
    print(f"{(df["FinalResult"].value_counts().at[1] / len(df.index)) * 100}%")
    print(BORDER)
    print("Percentage of Failed students")
    print(f"{(df["FinalResult"].value_counts().at[0] / len(df.index)) * 100}%")
    print(BORDER)
    print("Que: Is the Dataset balanced?")
    print("Ansewer: As dataset contins the passed students are 18 out of 30 which resulted in 60%\n"
          "and the failed students are 12 out of 30 which resulted in 40%. According to me, the word balanced\n"
          "referred to as equal ratio of result and we are learning about how to train the machine to get the\n"
          "maximum positive percentage or maximum prediction, but there may be a possibility that\n" 
          "a model can or can not predict the exact same ratio or accurance. Here the passed students percentage\n" 
          "is arguablly acceptable hence, I can say that this model is balanced.")


def main():
    analyse_dist_of_finalResult()

if __name__ == "__main__":
    main()