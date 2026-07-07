from functools import reduce

get_mapped_data = lambda num: num * 2

def check_prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def store_given_value_in_list(number):
    number_list = list()
    for num in range(1, number + 1):
        number_list.append(int(input(f"Enter number {num}: ")))
    
    return number_list

get_maximum_number = lambda num1, num2: num1 if num1 > num2 else num2

def main():
    print("----------------------------------------------------------------------")
    limit_number = int(input("Enter the limit number: "))

    given_list = store_given_value_in_list(limit_number)

    print("----------------------------------------------------------------------")
    print(f"Given list is {given_list}")
    print("----------------------------------------------------------------------")

    prime_numbers = list(filter(check_prime_number, given_list))
    print(f"Prime numbers in the list after filteration: {prime_numbers}")
    print("----------------------------------------------------------------------")

    mapped_data = list(map(get_mapped_data, prime_numbers))
    print(f"Mapped data with each element multiply by 2: {mapped_data}")
    print("----------------------------------------------------------------------")

    reduced_data = reduce(get_maximum_number, mapped_data)
    print(f"Maximum element from mapped data is: {reduced_data}")
    print("----------------------------------------------------------------------")

if __name__ == "__main__":
    main()