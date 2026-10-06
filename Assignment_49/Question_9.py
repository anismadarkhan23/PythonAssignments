from sklearn.metrics import classification_report

actual_values = [1, 1, 1, 1, 0, 0, 0, 0]
predicted_values = [1, 1, 0, 1, 0, 1, 0, 0]

print("Classification Report:")
print(classification_report(actual_values, predicted_values))