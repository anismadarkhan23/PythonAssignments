import os
import time
# import sys
from multiprocessing import Pool
from marvellous_getnumbers import store_given_value_in_list

def calculate_factorial_of_each_number_from_list(number):
    print(f"Running Process Id is: {os.getpid()}")

    factorial_of_number = 1
    for n in range(1, number + 1):
        factorial_of_number *= n
    
    print(f"Input number is: {number}")
    print(f"Factorial of {number} is {factorial_of_number}")

def main():
    # sys.set_int_max_str_digits(9999999999999) -> # OverflowError: Python int too large to convert to C int 
    limit_number = int(input("Enter number to get the list of integers: "))
    given_list_of_integers = store_given_value_in_list(limit_number)

    s_time = time.perf_counter()

    process_pool_obj = Pool()
    process_pool_obj.map(calculate_factorial_of_each_number_from_list, given_list_of_integers)
    process_pool_obj.close()
    process_pool_obj.join()

    e_time = time.perf_counter()

    print(f"Time required to complete the calculation is: {e_time - s_time:.2f} seconds")

if __name__ == "__main__":
    main()