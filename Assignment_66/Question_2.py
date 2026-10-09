import numpy as np
import math
import matplotlib.pyplot as plt

BORDER = "-" * 65

def ReLU(z):
    return max(0, z)

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def tanh(z):
    return math.tanh(z)

def plot_activation_functions():
    z_values = np.linspace(-10, 10, 400)
    relu_values = [ReLU(z) for z in z_values]
    sigmoid_values = [sigmoid(z) for z in z_values]
    tanh_values = [tanh(z) for z in z_values]

    plt.figure(figsize=(9, 6))
    plt.plot(z_values, relu_values, label="ReLU")
    plt.plot(z_values, sigmoid_values, label="Sigmoid")
    plt.plot(z_values, tanh_values, label="Tanh")
    plt.xlabel("Input (z)")
    plt.ylabel("Activation output")
    plt.title("Activation Functions")
    plt.axhline(0, color="black", linewidth=0.7)
    plt.axvline(0, color="black", linewidth=0.7)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()

def demonstrate_activation_functions(inputs, wights, bias):
    print(BORDER)
    print("Inputs are (X): ", inputs)

    print(BORDER)
    print("Wights are (W): ", wights)

    print(BORDER)
    print("Bias (b): ", bias)

    z = 0
    for i in range(len(inputs)):
        z = z + (inputs[i] * wights[i]) 

    z = z + bias
    print(BORDER)
    print(f"Weights Sum (z): {z:0.2f}")

    return z

def main():
    print("------------- DEMONSTRATION OF ACTIVATION FUNCTIONS -------------")

    inputs = [
        -10.0, 
        -9.0, 
        -8.0, 
        -7.0, 
        -6.0, 
        -5.0, 
        -4.0, 
        -3.0, 
        -2.0, 
        -1.0, 
        0, 
        10.0, 
        9.0, 
        8.0, 
        7.0, 
        6.0, 
        5.0, 
        4.0, 
        3.0, 
        2.0, 
        1.0
    ]

    weights = [
        0.6, 
        0.4, 
        -0.2,
        0.3,
        1.0,
        -1.2,
        -0.5,
        0.5,
        -0.8,
        0.9,
        0,
        0.2,
        0.1,
        -0.4,
        1.4,
        1.5,
        0.8,
        -0.6,
        -1.0
        -1.1,
        -0.8,
        1.1
    ]
    
    bias = 0.5

    weighted_sum = demonstrate_activation_functions(inputs, weights, bias)

    print(BORDER)
    print("------------------------------ ReLU -----------------------------")
    res_of_relu = ReLU(weighted_sum)
    print(f"y = {res_of_relu:0.2f}")
    print("------------------------------ ReLU -----------------------------")
    print(BORDER)

    print(BORDER)
    print("---------------------------- Sigmoid ----------------------------")
    res_of_sigmoid = sigmoid(weighted_sum)
    print(f"y = {res_of_sigmoid:0.2f}")
    print("---------------------------- Sigmoid ----------------------------")
    print(BORDER)

    print(BORDER)
    print("----------------------------- tanh ------------------------------")
    res_of_tanh = tanh(weighted_sum)
    print(f"y = {res_of_tanh:0.2f}")
    print("----------------------------- tanh ------------------------------")
    print(BORDER)

    plot_activation_functions()
    
    print("------------- DEMONSTRATION OF ACTIVATION FUNCTIONS -------------")

if __name__ == "__main__":
    main()