import time
from multiprocessing import Pool
from marvellous_getnumbers import store_given_value_in_list
from marvellous_check_prime_number import get_count_of_prime_number_till_input_number

def main():
    limit_number = int(input("Enter number to get the list of integers: "))
    given_list_of_integers = store_given_value_in_list(limit_number)

    s_time = time.perf_counter()

    pool_obj = Pool()
    pool_obj.map(get_count_of_prime_number_till_input_number, given_list_of_integers)
    pool_obj.close()
    pool_obj.join()

    e_time = time.perf_counter()

    print(f"Time required to complete the calculation is: {e_time - s_time:.2f} seconds")

if __name__ == "__main__":
    main()