import schedule
import time
import datetime

def display_message():
    print("Jay Ganesh...", datetime.datetime.now())

def main():
    schedule.every(2).seconds.do(display_message)

    while True:
        schedule.run_pending()
        time.sleep(0.1)

if __name__ == "__main__":
    main()