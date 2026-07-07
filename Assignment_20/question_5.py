import threading
import time

def display_one_to_fifty():
    for num in range(50):
        print(num + 1, end = " ")
    
    print()
    
def display_fifty_to_one():
    for num in range(50, 0, -1):
        print(num, end = " ")
    
    print()

def main():
    start_time = time.perf_counter()

    thread1 = threading.Thread(target = display_one_to_fifty)
    thread2 = threading.Thread(target = display_fifty_to_one)

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

    end_time = time.perf_counter()

    print(f"Time required to perform the both threads is {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()