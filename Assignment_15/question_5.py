from functools import reduce

get_max_number = lambda num1, num2: max(num1, num2)

def main():
    number_data = list()

    print("---------------------------------------------------")
    count_of_number_list = int(input("Enter the total count of number list: "))
    print("---------------------------------------------------")
    for i in range(count_of_number_list):
        number_data.append(int(input(f"Enter number {i + 1}: ")))

    print("---------------------------------------------------")
    print("Entered number list is: ", number_data)

    max_number = reduce(get_max_number, number_data)
    print("---------------------------------------------------")
    print("Maximum number from given list is: ", max_number)
    print("---------------------------------------------------")

if __name__ == "__main__":
    main()