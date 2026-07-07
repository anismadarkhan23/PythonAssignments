import threading
import time
import queue

def sum_of_elements(number_list, result_queue):
    total = 0
    for num in number_list:
        total += num
    
    result_queue.put(total)

def product_of_elements(number_list, result_queue):
    total_product = 1
    for num in number_list:
        total_product *= num
    
    result_queue.put(total_product)

def store_given_value_in_list(number):
    number_list = list()
    for num in range(1, number + 1):
        number_list.append(int(input(f"Enter number {num}: ")))
    
    return number_list

def main():
    limit_number = int(input("Enter the limit number: "))
    given_list = store_given_value_in_list(limit_number)

    start_time = time.perf_counter()

    thread1_queue = queue.Queue()
    thread2_queue = queue.Queue()

    thread1 = threading.Thread(target = sum_of_elements, args = (given_list, thread1_queue))
    thread2 = threading.Thread(target = product_of_elements, args = (given_list, thread2_queue))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"Result of thread 1 is {thread1_queue.get()}")
    print(f"Result of thread 2 is {thread2_queue.get()}")

    end_time = time.perf_counter()
    print(f"Time required to perform the both threads is {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()