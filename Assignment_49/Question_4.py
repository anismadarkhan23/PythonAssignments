# Program to calculate the Euclidean distance between two points before & after applying feature sscaling.
import math

def calculate_euclidean_distance(pt1, pt2):
    distance = math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
    return distance

def main():
    point1 = [2, 3]
    point2 = [5, 7]

    distance_before_scaling = calculate_euclidean_distance(point1, point2)
    print(f"Euclidean distance between {point1} and {point2} before scaling: {distance_before_scaling}")
    print("-" * 50)

    # Apply feature scaling (min-max normalization)
    min_x = min(point1[0], point2[0])
    max_x = max(point1[0], point2[0])
    min_y = min(point1[1], point2[1])
    max_y = max(point1[1], point2[1])

    print(f"Min value for x: {min_x}")
    print(f"Max value for x: {max_x}")
    print(f"Min value for y: {min_y}")
    print(f"Max value for y: {max_y}")
    print("-" * 50)

    scaled_point1 = [(point1[0] - min_x) / (max_x - min_x), (point1[1] - min_y) / (max_y - min_y)]
    scaled_point2 = [(point2[0] - min_x) / (max_x - min_x), (point2[1] - min_y) / (max_y - min_y)]
    print(f"Scaled point 1: {scaled_point1}")
    print(f"Scaled point 2: {scaled_point2}")
    print("-" * 50)

    distance_after_scaling = calculate_euclidean_distance(scaled_point1, scaled_point2)
    print(f"Euclidean distance between {scaled_point1} and {scaled_point2} after scaling: {distance_after_scaling}")
    print("-" * 50)

if __name__ == "__main__":
    main()
