import schedule
import time
from datetime import datetime

def display_do_coding_message():
    print(f"Current time is {datetime.now().strftime('%I:%M:%S %p')} & message printed as 'Coding Kar...👨🏻‍💻'")

def main():
    schedule.every(30).minutes.do(display_do_coding_message)

    while True:
        schedule.run_pending()
        time.sleep(20)

if __name__ == "__main__":
    main()