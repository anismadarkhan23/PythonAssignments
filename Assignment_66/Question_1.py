import numpy as np
import math

BORDER = "-"*30

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def main():
    print(BORDER)
    input = np.array([2.0, 3.0])
    print("X: ", input)

    print(BORDER)
    wights = np.array([0.4, 0.6])
    print("W: ", wights)

    print(BORDER)
    bias = 0.5
    print("b: ", bias)

    print(BORDER)
    z = np.dot(input, wights) + bias
    print(f"z: {z:.2f}")

    print(BORDER)
    Y = sigmoid(z)
    print(f"Y: {Y:.2f}")

    print(BORDER)
    if Y >= 0.5:
        print("Output is close to 1")
    else:
        print("Output is close to 0")

    print(BORDER)
    
if __name__ == "__main__":
    main()