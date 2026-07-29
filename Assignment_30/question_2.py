import schedule
import time
from datetime import datetime

def display_date_and_time():
    print("Current Date and Time: ", datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

def main():
    schedule.every(1).minute.do(display_date_and_time)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()