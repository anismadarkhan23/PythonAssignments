import math
import numpy as np

BORDER = "-" * 80

def calculate_loss_with_MSE(actual_values, predicted_values, sample_size):
    total_calculated_error = 0

    for sample in range(sample_size):
        error = actual_values[sample] - predicted_values[sample]
        total_calculated_error = total_calculated_error + (error ** 2)

    mean_squared_error = total_calculated_error / sample_size
    return mean_squared_error

def calculate_loss_with_BCE(actual_values, predicted_values, sample_size):
    # -(1/N) * sum(y_i * log(y_cap_i) + (1 - y_i) * log(1 - y_cap_i))

    total_calculated_error = 0

    epsilon_value = 1e-15

    for sample in range(sample_size):
        y_i = actual_values[sample]

        y_cap_i = max(min(predicted_values[sample], 1.0 - epsilon_value), epsilon_value)    

        term_i = y_i * math.log(y_cap_i) + (1.0 - y_i) * math.log(1.0 - y_cap_i)
        
        total_calculated_error += term_i

    binary_cross_entropy = -(1.0 / sample_size) * total_calculated_error
    return binary_cross_entropy

def main():
    y_true = [10, 12, 14, 16, 18, 20, 22]
    y_predicted = [12, 14, 16, 18, 20, 22, 22]

    data_size = len(y_true)

    MSE = calculate_loss_with_MSE(y_true, y_predicted, data_size)
    print(BORDER)
    print("------------------- LOSS CALCULATION WITH MEAN SQUARED ERROR -------------------")
    print(f"MSE -> Actual values: {y_true}")
    print(f"MSE -> Predicted values: {y_predicted}")
    print(f"Loss using Mean Squared Error(MSE) is {MSE:.2f}")
    print("------------------- LOSS CALCULATION WITH MEAN SQUARED ERROR -------------------")
    print(BORDER)

    y_true =      [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]
    y_predicted = [0.95, 1, 0.10, 0, 0.78, 0.90, 0.88, 0.13, 0, 0.99, 0.23]

    data_size = len(y_true)

    BSE = calculate_loss_with_BCE(y_true, y_predicted, data_size)
    print(BORDER)
    print("------------------ LOSS CALCULATION WITH BINARY CROSS ENTROPY ------------------")
    print(f"BSE -> Actual values: {y_true}")
    print(f"BSE -> Predicted values: {y_predicted}")
    print(f"Loss using Binary Cross Entropy(BSE) is {BSE:.2f}")
    print("------------------ LOSS CALCULATION WITH BINARY CROSS ENTROPY ------------------")
    print(BORDER)

if __name__ == "__main__":
    main()