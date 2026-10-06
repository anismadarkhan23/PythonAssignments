# Question: Explain the concept of Classification report in machine learning?
# Answer: 
# 1. Classification report is performance evaluation summary used in Machine Learning to evaluate the performance 
# of a classification model. Instead of just providing a single accuracy score, it provides a detailed breakdown of the model's 
# performance across different classes.
# 2. It provides detailed summary of the precision, recall, F1-score, and support for each class in a classification problem. 
# 3. The classification report is based on four concepts of Confustion Matri which is
#   - True Positives (TP): Model correctly predicts the positive class.
#   - True Negatives (TN): Model correctly predicts the negative class.
#   - False Positives (FP): Model incorrectly predicts the positive class.
#   - False Negatives (FN): Model incorrectly predicts the negative class.
# 4. Precision: It measures the accuracy among the predicted postive values.
#   - Precision = True Positives / (True Positives + False Positives)
# 5. Recall: It measures the ability of the model to find all the relevant cases (true positives) within a dataset.
#   - Recall = True Positives / (True Positives + False Negatives)
# 6. F1-score: It is the mean of precision and recall, providing a balance between the two metrics. 
# It is especially useful when the class distribution is imbalanced.
#   - F1-score = 2 * (Precision * Recall) / (Precision + Recall)
# 7. Support: It indicates the number of actual occurrences of each class in the dataset.
#   - Support = Number of occurrences of each class in the dataset

# Why is it used?
# A classification report is used in machine learning because on the basis of 
# overall accuracy is rarely enough to evaluate whether a model actually works in practice.
# Its primary purpose is to provide a granular, class-by-class audit of model predictions, 
# ensuring you catch hidden failure modes before deployment.

# What type of models requires it?
# A classification report is required specifically for classification models—algorithms whose objective is to predict a
# categorical data, class label, or probability distribution across distinct groups.
# It applies on Binary Classifications, Multiclass Classifications, etc. Some common classification models include:
# - Logistic Regression
# - Decision Trees
# - Random Forests
# - k-Nearest Neighbors (k-NN)