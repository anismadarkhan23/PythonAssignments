# Question: In Classification report, explain the meaning of the following metrics?
# 1. Precision
# 2. Recall
# 3. F1-score
# 4. Support
# 5. Auccuracy

# Answer: 
# 1. The classification report is based on four concepts of Confustion Matri which is
#   - True Positives (TP): Model correctly predicts the positive class.
#   - True Negatives (TN): Model correctly predicts the negative class.
#   - False Positives (FP): Model incorrectly predicts the positive class.
#   - False Negatives (FN): Model incorrectly predicts the negative class.
# 2. Precision: It measures the accuracy among the predicted postive values.
#   - Precision = True Positives / (True Positives + False Positives)
# 3. Recall: It measures the ability of the model to find all the relevant cases (true positives) within a dataset.
#   - Recall = True Positives / (True Positives + False Negatives)
# 4. F1-score: It is the mean of precision and recall, providing a balance between the two metrics. 
# It is especially useful when the class distribution is imbalanced.
#   - F1-score = 2 * (Precision * Recall) / (Precision + Recall)
# 5. Support: It indicates the number of actual occurrences of each class in the dataset.
#   - Support = Number of occurrences of each class in the dataset
# 6. Accuracy: It measures the overall correctness of the model's predictions.
#   - Accuracy = (True Positives + True Negatives) / (True Positives + True Negatives + False Positives + False Negatives)
