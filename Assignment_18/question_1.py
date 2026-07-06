from functools import reduce

addition_of_all_numbers = lambda num1, num2: num1 + num2

def store_given_value_in_list(number):
    number_list = list()
    for num in range(1, number + 1):
        number_list.append(int(input(f"Enter number {num}: ")))
    
    return number_list

def main():
    print("------------------------------------------------")
    limit_number = int(input("Enter the limit number: "))

    given_list = store_given_value_in_list(limit_number)

    print("------------------------------------------------")
    print(f"Given list is {given_list}")
    print("------------------------------------------------")

    sum_of_numbers = reduce(addition_of_all_numbers, given_list)

    print(f"Sum of numbers given in list is: {sum_of_numbers}")
    print("------------------------------------------------")

if __name__ == "__main__":
    main()
    