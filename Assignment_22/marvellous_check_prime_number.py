import os

def check_prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_count_of_prime_number_till_input_number(number):
    print(f"Running Process Id is: {os.getpid()}")

    prime_numbers_count = 0
    
    for n in range(number + 1):
        if check_prime_number(n):
            prime_numbers_count += 1
        
    print(f"Input number is: {number}")
    print(f"Total prime numbers till {number} is {prime_numbers_count}")