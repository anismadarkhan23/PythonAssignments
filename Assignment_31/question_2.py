import schedule
import time

def DisplayMessage(given_message):
    print(given_message)

def main():
    message = input("Enter the message to display on specific time interval: ")

    schedule.every(5).seconds.do(DisplayMessage, message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()