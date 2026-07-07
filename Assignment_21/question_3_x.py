import threading
import time

count = 0
thread_lock = threading.Lock()

def counter():
    print(f"{threading.current_thread().name} running completed")
    global count
    thread_lock.acquire()
    try:
        temp_count = count
        count = temp_count + 1
    finally:
        thread_lock.release()

def main():
    thread1 = threading.Thread(target = counter)
    thread2 = threading.Thread(target = counter)
    thread3 = threading.Thread(target = counter)
    thread4 = threading.Thread(target = counter)
    thread5 = threading.Thread(target = counter)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()


    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()

    print(f"Final counter is {count}")

if __name__ == "__main__":
    main()