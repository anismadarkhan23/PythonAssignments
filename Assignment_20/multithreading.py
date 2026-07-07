import threading
import time

def get_first_ten_even_numbers(given_num):
    first_ten_even_numbers = list()
    number = 1
    while number <= given_num:
        first_ten_even_numbers.append(number * 2)
        number += 1
    
    print(f"First {given_num} even numbers are: {first_ten_even_numbers}")

def get_first_ten_odd_numbers(given_num):
    first_ten_odd_numbers = list()
    number = 0
    while number < given_num:
        first_ten_odd_numbers.append((number * 2) + 1)
        number += 1
    
    print(f"First {given_num} odd numbers are: {first_ten_odd_numbers}")

def main():
    print("-------------- Get first 10000000 Even & Odd Numbers -------------")
    start_time = time.perf_counter()

    thread_obj1 = threading.Thread(target = get_first_ten_even_numbers, args = (10000000, ))
    thread_obj2 = threading.Thread(target = get_first_ten_odd_numbers, args = (10000000, ))

    thread_obj1.start()
    thread_obj2.start()

    thread_obj1.join()
    thread_obj2.join()

    end_time = time.perf_counter()

    print(f"Time required to get first 10000000 even & odd numbers is {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()