def get_maximum_number(number_list):
    maximum_num = 0
    for num in number_list:
        if num > maximum_num:
            maximum_num = num
    
    return maximum_num

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

    maximum_number = get_maximum_number(given_list)

    print(f"Maximum number from given list is: {maximum_number}")
    print("------------------------------------------------")

if __name__ == "__main__":
    main()