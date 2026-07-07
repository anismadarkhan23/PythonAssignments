import threading
import time
from functools import reduce
import marvellous_getnumbers

get_addition = lambda num1, num2: num1 + num2
get_even_elements = lambda num: num % 2 == 0
get_odd_elements = lambda num: num % 2 != 0

def EvenList(number_list):
    even_elements = list(filter(get_even_elements, number_list))
    sum_of_even_elements = reduce(get_addition, even_elements)
    print(f"Sum of even elements are: {sum_of_even_elements}")

def OddList(number_list):
    odd_elements = list(filter(get_odd_elements, number_list))
    sum_of_odd_elements = reduce(get_addition, odd_elements)
    print(f"Sum of odd elements are: {sum_of_odd_elements}")

def main():
    print("--------------------------- Start of main ---------------------------")
    limit_number = int(input("Enter the limit number: "))
    given_list = marvellous_getnumbers.store_given_value_in_list(limit_number)

    start_time = time.perf_counter()

    thread_evenList = threading.Thread(target = EvenList, args = (given_list, ))
    thread_oddList = threading.Thread(target = OddList, args = (given_list, ))

    thread_evenList.start()
    thread_oddList.start()

    thread_evenList.join()
    thread_oddList.join()

    end_time = time.perf_counter()
    print(f"Time required to perform the both threads is {end_time - start_time:.4f} seconds")
    print("--------------------------- Exit from main --------------------------")

if __name__ == "__main__":
    main()