import numpy as np
import math

BORDER = "-"*45

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def main():
    print(BORDER)
    inputs = np.array([0.1, 0.3, 0.5, 0.2, 0.4])
    print("Input (x): ", inputs)

    weights = np.array([0.4, 0.6, 0.3, 0.2, 0.5])
    print("Initial Weights (w): ", weights)

    bias = 0.3
    print("Initial Bias (b): ", bias)

    target_output = 1.0
    print("Target Output (y): ", target_output)

    learning_rate = 0.1
    print("Learning Rate: ", learning_rate)
    print(BORDER)

    print("------------ First Forward Pass -------------")
    z = np.dot(inputs, weights) + bias
    print(f"Linear combination (z): {z:.2f}")

    y_cap = sigmoid(z)
    print(f"Prediction (y_cap): {y_cap:.2f}")
    print(BORDER)

    error = target_output - y_cap
    print("----------------- Error ---------------------")
    print(f"Error: {error:.2f}")
    print(BORDER)

    sigmoid_derivative = y_cap * (1.0 - y_cap)

    # Delta term (gradient factor): - (y - y_hat) * sigmoid'(z)
    # dE/dz = -(target - y_hat) * y_hat * (1 - y_hat)
    delta = -error * sigmoid_derivative

    # Store previous weights to display comparision
    old_weights = list(weights)
    old_bias = bias

    # Gradient descent update: w = w - learning_rate * (dE/dw)
    # where dE/dw_j = delta * x_j
    updated_weights = []
    for j in range(len(weights)):
        grad_w = delta * inputs[j]
        new_w = weights[j] - (learning_rate * grad_w)
        updated_weights.append(new_w)

    # Bias update: b = b - learning_rate * delta
    grad_b = delta * 1.0
    updated_bias = bias - (learning_rate * grad_b)

    print("--- WEIGHT & BIAS UPDATE SUMMARY ---")
    for i, (w_old, w_new) in enumerate(zip(old_weights, updated_weights), start=1):
        delta_w = w_new - w_old
        print(f"Weight w{i}: Old = {w_old:.2f} -> New = {w_new:.2f}  (Change: {delta_w:+.2f})")

    delta_b = updated_bias - old_bias
    print(f"Bias b   : Old = {old_bias:.2f} -> New = {updated_bias:.2f}  (Change: {delta_b:+.2f})")
    
if __name__ == "__main__":
    main()