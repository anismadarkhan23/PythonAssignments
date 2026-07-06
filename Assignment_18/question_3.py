def get_minimum_number(number_list):
    minimum_num = number_list[0]

    for num in number_list:
        if num < minimum_num:
            minimum_num = num

    return minimum_num

def store_given_value_in_list(number):
    number_list = list()
    for num in range(1, number + 1):
        number_list.append(int(input(f"Enter number {num}: ")))
    
    return number_list

def main():
    limit_number = int(input("Enter the limit number: "))

    given_list = store_given_value_in_list(limit_number)

    print("------------------------------------------------")
    print(f"Given list is {given_list}")
    print("------------------------------------------------")

    minimum_number = get_minimum_number(given_list)

    print(f"Minimum number from given list is: {minimum_number}")
    print("------------------------------------------------")

if __name__ == "__main__":
    main()