import threading
import time

def Small(string):
    count = 0
    for character in string:
        if 'a' <= character <= 'z':
            count += 1

    print(f"Thread Id of Small is {threading.get_ident()}")
    print(f"Thread name is: {threading.current_thread().name}")
    print(f"Number of lowercase characters in {string} is {count}")

def Capital(string):
    count = 0
    for character in string:
        if 'A' <= character <= 'Z':
            count += 1

    print(f"Thread Id of Capital is {threading.get_ident()}")
    print(f"Thread name is: {threading.current_thread().name}")
    print(f"Number of uppercase characters in {string} is {count}")

def Digits(string):
    count = 0
    for character in string:
        if '0' <= character <= '9':
            count += 1
        
    print(f"Thread Id of Digits is {threading.get_ident()}")
    print(f"Thread name is: {threading.current_thread().name}")
    print(f"Number of numeric digits in {string} is {count}")

def main():
    print("--------------------------- Start of main ---------------------------")
    given_string = input("Enter the string: ")

    start_time = time.perf_counter()

    thread_small = threading.Thread(target = Small, args = (given_string, ))
    thread_capital = threading.Thread(target = Capital, args = (given_string, ))
    thread_digits = threading.Thread(target = Digits, args = (given_string, ))

    thread_small.start()
    thread_capital.start()
    thread_digits.start()

    thread_small.join()
    thread_capital.join()
    thread_digits.join()

    end_time = time.perf_counter()
    print(f"Time required to perform the both threads is {end_time - start_time:.4f} seconds")
    print("--------------------------- Exit from main --------------------------")

if __name__ == "__main__":
    main()