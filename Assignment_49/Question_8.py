from sklearn.metrics import confusion_matrix

actual_values = [1, 1, 1, 1, 0, 0, 0, 0]
predicted_values = [1, 1, 0, 1, 0, 1, 0, 0]

cm = confusion_matrix(actual_values, predicted_values)

print("Confusion Matrix:")
print(cm)