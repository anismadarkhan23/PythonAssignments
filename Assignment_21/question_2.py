import threading
import time

def get_maximum_number(number_list):
    maximum_number = 0
    for num in number_list:
        if num > maximum_number:
            maximum_number = num
        
    print(f"Maximum number is: {maximum_number}")

def get_minimum_number(number_list):
    minimum_number = number_list[0]
    for num in number_list:
        if num < minimum_number:
            minimum_number = num
    
    print(f"Minimum number is: {minimum_number}")

def store_given_value_in_list(number):
    number_list = list()
    for num in range(1, number + 1):
        number_list.append(int(input(f"Enter number {num}: ")))
    
    return number_list

def main():
    limit_number = int(input("Enter the limit number: "))
    given_list = store_given_value_in_list(limit_number)

    start_time = time.perf_counter()

    maximum_thread = threading.Thread(target = get_maximum_number, args = (given_list, ))
    minimum_thread = threading.Thread(target = get_minimum_number, args = (given_list, ))

    maximum_thread.start()
    minimum_thread.start()

    maximum_thread.join()
    minimum_thread.join()

    end_time = time.perf_counter()

    print(f"Time required to perform the both threads is {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()