import math

BORDER = "-" * 75

def calculate_distance_bet_two_coordinates(point_1, point_2):
    distance = math.sqrt(((point_1["X"] - point_2["X"]) ** 2) + ((point_1["Y"] - point_2["Y"]) ** 2))
    return f"{distance:.2f}"

def predict_class_for_coordinates(k_neighbour):

    coordinate_data = [
        {"Point": "A", "X": 1, "Y": 2, "Label": "Red"},
        {"Point": "B", "X": 2, "Y": 3, "Label": "Blue"},
        {"Point": "C", "X": 3, "Y": 1, "Label": "Red"},
        {"Point": "D", "X": 6, "Y": 5, "Label": "Blue"},
        {"Point": "E", "X": 4, "Y": 3, "Label": "Red"},
        {"Point": "F", "X": 2, "Y": 4, "Label": "Red"},
        {"Point": "G", "X": 8, "Y": 7, "Label": "Blue"},
    ]

    print(BORDER)
    print("Coordinate data is as below")
    print(BORDER)
    for coordinate in coordinate_data:
        print(coordinate)

    print(BORDER)

    X_new_point = int(input("Enter the new X coordinate: "))
    Y_new_point = int(input("Enter the new Y coordinate: "))

    new_coordinate = dict()
    new_coordinate["X"] = X_new_point
    new_coordinate["Y"] = Y_new_point

    print(BORDER)
    print("New coordinates is as below")
    print(new_coordinate)
    print(BORDER)

    for coordinate in coordinate_data:
        coordinate["c_distance"] = calculate_distance_bet_two_coordinates(coordinate, new_coordinate)

    print("Displaying coordinates data with distance to new coordinate point")
    print(BORDER)
    for coordinate in coordinate_data:
        print(coordinate)

    print(BORDER)

    sorted_coordinates = sorted(coordinate_data, key = lambda data: data["c_distance"])
    print("Displaying coordinates data with distance to new coordinate point")
    print(BORDER)    
    for s_coordinate in sorted_coordinates:
        print(s_coordinate)

    print(BORDER)

    nearest_coordinates = sorted_coordinates[:k_neighbour]
    print("Displaying nearest coordinates data")
    print(BORDER)    
    for n_coordinate in nearest_coordinates:
        print(n_coordinate)

    print(BORDER)

    r_votes = 0
    b_votes = 0
    for coordinate in nearest_coordinates:
        if coordinate["Label"] == "Red":
            r_votes += 1
        else:
            b_votes += 1

    if r_votes > b_votes:
        print(f"The class of coordinate ({new_coordinate["X"]}, {new_coordinate["Y"]}) is Red")
        print(BORDER)
    else:
        print(f"The class of coordinate ({new_coordinate["X"]}, {new_coordinate["Y"]}) is Blue")
        print(BORDER)

def main():
    print(BORDER)
    neighbour_value = int(input("Enter the neighbour value: "))

    predict_class_for_coordinates(neighbour_value)

if __name__ == "__main__":
    main()