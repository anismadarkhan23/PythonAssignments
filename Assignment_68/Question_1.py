import numpy as np

BORDER = "-"*50

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
            print(region)
                
            # Multiply & Sum i.e. apply conval operation
            result = np.sum(region * kernel)

            # Store the result into feature map
            feature_map[i][j] = result

    print("Feature map (Detected Edge)")
    print(feature_map)
    print(BORDER)

def main():
    generate_feature_map()

if __name__ == "__main__":
    main()

