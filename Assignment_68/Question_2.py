import numpy as np

BORDER = "-"*50

def apply_max_pooling(converted_feature_map):

    max_pooling_matrics = np.zeros((2, 2))

    for i in range(2):
        print(f"Step {i+1}")
        for j in range(2):
            region = converted_feature_map[i:i+2, j:j+2]

            print(region)

            max_pooling_matrics[i][j] = np.max(region)

    print("Max Pooling Result (2*2)")
    print(max_pooling_matrics)
    return max_pooling_matrics

def ReLU(x):
    return max(0, x)

def convert_feature_map_using_relu():
    feature_map = generate_feature_map()

    converted_feature_map = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            result = ReLU(feature_map[i][j])

            converted_feature_map[i][j] = result

    print("Converted Feature map using ReLU")
    print(converted_feature_map)
    print(BORDER)

    apply_max_pooling(converted_feature_map)

def generate_feature_map():
    image = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ])

    print(BORDER)
    print("Original 5*5 Image")
    print(image)
    print(BORDER)

    kernel = np.array([
        [-1, -1, -1],
        [0, 0, 0],
        [1, 1, 1],
    ])

    print("Kernel 3*3")
    print(kernel)
    print(BORDER)

    # (((N - M) + 1) * ((N - M) + 1))
    feature_map = np.zeros((3, 3))

    for i in range(3):
        for j in range(3):

            # Extract first 3*3 region
            region = image[i:i+3, j:j+3]

            # Multiply & Sum i.e. apply conval operation
            result = np.sum(region * kernel)

            # Store the result into feature map
            feature_map[i][j] = result

    print("Feature map (Detected Edge)")
    print(feature_map)
    print(BORDER)

    return feature_map
    
def main():
    convert_feature_map_using_relu()

if __name__ == "__main__":
    main()

