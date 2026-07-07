import threading
import time

def get_prime_numbers(number_list):
    prime_numbers = []
    for num in number_list:
        if check_prime_number(num):
            prime_numbers.append(num)
    
    print(f"Prime numbers are: {prime_numbers}")

def get_non_prime_numbers(number_list):
    non_prime_numbers = []
    for num in number_list:
        if check_prime_number(num) is False:
            non_prime_numbers.append(num)
    
    print(f"Non-Prime numbers are: {non_prime_numbers}")

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

def main():
    limit_number = int(input("Enter the limit number: "))
    given_list = store_given_value_in_list(limit_number)

    start_time = time.perf_counter()

    prime_thread = threading.Thread(target = get_prime_numbers, args = (given_list, ))
    non_prime_thread = threading.Thread(target = get_non_prime_numbers, args = (given_list, ))

    prime_thread.start()
    non_prime_thread.start()

    prime_thread.join()
    non_prime_thread.join()

    end_time = time.perf_counter()

    print(f"Time required to perform the both threads is {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()