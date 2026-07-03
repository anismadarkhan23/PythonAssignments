from functools import reduce

get_sum_of_numbers = lambda num1, num2: num1 + num2

def main():
    number_data = list()

    print("---------------------------------------------------")
    count_of_number_list = int(input("Enter the total count of number list: "))
    print("---------------------------------------------------")
    for i in range(count_of_number_list):
        number_data.append(int(input(f"Enter number {i + 1}: ")))

    print("---------------------------------------------------")
    print("Entered number list is: ", number_data)

    addition = reduce(get_sum_of_numbers, number_data)
    print("---------------------------------------------------")
    print("Addition of numbers from given list is: ", addition)
    print("---------------------------------------------------")

if __name__ == "__main__":
    main()