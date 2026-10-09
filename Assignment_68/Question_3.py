import numpy as np

BORDER = "-"*60

matrix = np.array([
    [6, 4],
    [8, 6]
])

print(BORDER)
print("Given Matrix is")
print(matrix)
print(BORDER)

# Convert the 2D matrix into a 1D input vector in row-major order.
flattened_matrix = matrix.flatten()

print("Flatten layer")
print(flattened_matrix)
print(BORDER)

# Each row contains the weights from one input; each column is one output neuron.
fully_connected_weights = np.array([
    [0.1, 0.2],
    [0.2, 0.1],
    [0.3, 0.4],
    [0.4, 0.3]
])
fully_connected_biases = np.array([0.5, 1.0])

print("Fully Connected Weights")
print(fully_connected_weights)
print(BORDER)

print("Fully Connected Biases")
print(fully_connected_biases)
print(BORDER)

final_output = []

print("Fully Connected Layer: output = sum(input * weight) + bias")
print(BORDER)

for neuron in range(fully_connected_weights.shape[1]):
    # Multiply each input by its weight, then add the neuron's bias.
    weighted_inputs = flattened_matrix * fully_connected_weights[:, neuron]
    bias = fully_connected_biases[neuron]
    output = sum(weighted_inputs) + bias
    final_output.append(output)
    print(f"Neuron {neuron + 1}: {weighted_inputs} + {bias} = {output:.2f}")

print(BORDER)
print("Final output")
print(np.array(final_output))
print(BORDER)


