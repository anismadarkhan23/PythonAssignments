actual_values = [1, 1, 1, 1, 0, 0, 0, 0]
predicted_values = [1, 1, 0, 1, 0, 1, 0, 0]

true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0

for i in range(len(actual_values)):
    if actual_values[i] == 1 and predicted_values[i] == 1:
        true_positives += 1
    elif actual_values[i] == 0 and predicted_values[i] == 0:
        true_negatives += 1
    elif actual_values[i] == 0 and predicted_values[i] == 1:
        false_positives += 1
    elif actual_values[i] == 1 and predicted_values[i] == 0:
        false_negatives += 1

print("True Positives (TP):", true_positives)
print("True Negatives (TN):", true_negatives)
print("False Positives (FP):", false_positives)
print("False Negatives (FN):", false_negatives)