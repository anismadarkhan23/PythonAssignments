import os
from multiprocessing import Pool
import time
import marvellous_getnumbers

def calculate_sum_of_squares(number):
    print(f"PID of running process is: {os.getpid()}")

    total_of_squares = 0
    for n in range(1, number + 1):
        total_of_squares = total_of_squares + (n ** 2)
    
    return total_of_squares

def main():
    limit_number = int(input("Enter number to get the list of integers: "))
    given_list_of_integers = marvellous_getnumbers.store_given_value_in_list(limit_number)

    s_time = time.perf_counter()

    process_pool_obj = Pool()
    sum_of_squares = process_pool_obj.map(calculate_sum_of_squares, given_list_of_integers)
    process_pool_obj.close()
    process_pool_obj.join()

    e_time = time.perf_counter()

    print(f"Sum of Squares is {sum_of_squares}")
    print(f"Time required to complete the calculation is: {e_time - s_time:.2f} seconds")

if __name__ == "__main__":
    main()
