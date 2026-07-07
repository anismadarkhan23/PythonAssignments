import threading
import time

def get_first_ten_even_numbers():
    first_ten_even_numbers = list()
    number = 1
    while number <= 10:
        first_ten_even_numbers.append(number * 2)
        number += 1
    
    print(f"First 10 even numbers are: {first_ten_even_numbers}")

def get_first_ten_odd_numbers():
    first_ten_odd_numbers = list()
    number = 0
    while number < 10:
        first_ten_odd_numbers.append((number * 2) + 1)
        number += 1
    
    print(f"First 10 odd numbers are: {first_ten_odd_numbers}")

def main():
    
    start_time = time.perf_counter()

    thread_obj1 = threading.Thread(target = get_first_ten_even_numbers)
    thread_obj2 = threading.Thread(target = get_first_ten_odd_numbers)

    thread_obj1.start()
    thread_obj2.start()

    thread_obj1.join()
    thread_obj2.join()

    end_time = time.perf_counter()

    print(f"Time required to perform the both threads is {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()