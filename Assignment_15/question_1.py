get_square_numbers = lambda num: num * num

def main():
    number_data = list()

    print("---------------------------------------------------")
    count_of_number_list = int(input("Enter the total count of number list: "))
    print("---------------------------------------------------")
    for i in range(count_of_number_list):
        number_data.append(int(input(f"Enter number {i + 1}: ")))
    
    print("---------------------------------------------------")
    print("Entered number list is: ", number_data)

    squared_numbers = list(map(get_square_numbers, number_data))
    print("---------------------------------------------------")
    print("Squared number list is: ", squared_numbers)
    print("---------------------------------------------------")

if __name__ == "__main__":
    main()