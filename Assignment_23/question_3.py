import os
import time
from multiprocessing import Pool
from marvellous_getnumbers import store_given_value_in_list

def calculate_total_even_numbers_till(number):
    total_even_numbers = 0

    for n in range(1, number + 1):
        if n % 2 == 0:
            total_even_numbers += 1

    print(f"Process Id : {os.getpid()}")
    print(f"Input number : {number}")
    print(f"Total Even numbers till {number} : {total_even_numbers}")

def main():
    limit_number = int(input("Enter number to get the list of integers: "))
    given_list_of_integers = store_given_value_in_list(limit_number)

    s_time = time.perf_counter()

    pool_obj = Pool()
    pool_obj.map(calculate_total_even_numbers_till, given_list_of_integers)
    pool_obj.close()
    pool_obj.join()

    e_time = time.perf_counter()

    print(f"Time required to complete the calculation is: {e_time - s_time:.2f} seconds")

if __name__ == "__main__":
    main()