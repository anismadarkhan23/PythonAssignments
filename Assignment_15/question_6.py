from functools import reduce

get_min_number = lambda num1, num2: min(num1, num2)

def main():
    number_data = list()

    print("---------------------------------------------------")
    count_of_number_list = int(input("Enter the total count of number list: "))
    print("---------------------------------------------------")
    for i in range(count_of_number_list):
        number_data.append(int(input(f"Enter number {i + 1}: ")))

    print("---------------------------------------------------")
    print("Entered number list is: ", number_data)

    min_number = reduce(get_min_number, number_data)
    print("---------------------------------------------------")
    print("Minimum number from given list is: ", min_number)
    print("---------------------------------------------------")

if __name__ == "__main__":
    main()