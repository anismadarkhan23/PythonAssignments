import os
import time
from multiprocessing import Pool
from marvellous_getnumbers import store_given_value_in_list

def calculate_sum_power_of_five(number):
    print(f"Running Process Id is: {os.getpid()}")

    sum_power_of_five = 0

    for n in range(number + 1):
        sum_power_of_five += (n ** 5) 

    print(f"Input number is: {number}")
    print(f"Sum of power of five till {number} is {sum_power_of_five}")

def main():
    limit_number = int(input("Enter number to get the list of integers: "))
    given_list_of_integers = store_given_value_in_list(limit_number)

    s_time = time.perf_counter()

    p_obj = Pool()
    p_obj.map(calculate_sum_power_of_five, given_list_of_integers)
    p_obj.close()
    p_obj.join()

    e_time = time.perf_counter()

    print(f"Time required to complete the calculation is: {e_time - s_time:.2f} seconds")

if __name__ == "__main__":
    main()