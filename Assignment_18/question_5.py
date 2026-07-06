from functools import reduce
import MarvellousNum

addition_of_prime_numbers = lambda num1, num2: num1 + num2

def ListPrime(number_list):
    prime_list = list()
    for num in number_list:
        if MarvellousNum.ChkPrime(num):
            prime_list.append(num)
    
    return prime_list

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

    prime_numbers = ListPrime(given_list)
    print(f"Prime numbers list is: {prime_numbers}")
    print("------------------------------------------------")
    
    print(f"Addition of prime numbers from {prime_numbers} is {reduce(addition_of_prime_numbers, prime_numbers)}")
    print("------------------------------------------------")


if __name__ == "__main__":
    main()