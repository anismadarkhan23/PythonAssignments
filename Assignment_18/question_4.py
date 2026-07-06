def get_frequency_of_searched_number(number_list, given_number):
    count = 0
    for num in number_list:
        if num == given_number:
            count += 1
        
    return count

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

    searched_number = int(input("Enter the number to be searched: "))
    print("------------------------------------------------")
    
    frequency_of_number = get_frequency_of_searched_number(given_list, searched_number)

    print(f"Frequency of {searched_number} from given list is: {frequency_of_number}")
    print("------------------------------------------------")

if __name__ == "__main__":
    main()