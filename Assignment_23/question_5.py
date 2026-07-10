import os
import time
from multiprocessing import Pool
from marvellous_getnumbers import store_given_value_in_list

def calculate_factorial_till_given_number(number):
    factorial_till_number = 1

    for n in range(1, number + 1):
        factorial_till_number *= n

    print(f"Process Id : {os.getpid()}")
    print(f"Input number : {number}")
    print(f"Factorial till {number} : {factorial_till_number}")

def main():
    limit_number = int(input("Enter number to get the list of integers: "))
    given_list_of_integers = store_given_value_in_list(limit_number)

    s_time = time.perf_counter()

    pool_obj = Pool()
    pool_obj.map(calculate_factorial_till_given_number, given_list_of_integers)
    pool_obj.close()
    pool_obj.join()

    e_time = time.perf_counter()

    print(f"Time required to complete the calculation is: {e_time - s_time:.2f} seconds")

if __name__ == "__main__":
    main()