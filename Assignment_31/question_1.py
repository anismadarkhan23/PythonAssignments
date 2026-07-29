import schedule
import time

def main():
    message = input("Enter the message to display on specific time interval: ")
    time_interval = float(input("Enter the time in seconds: "))

    schedule.every(time_interval).seconds.do(print, message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()