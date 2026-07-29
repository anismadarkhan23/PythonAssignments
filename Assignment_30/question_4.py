import schedule
import time
from datetime import datetime

def display_namskar_everyday():
    print("Namskar...🙏🏻", datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

def main():
    schedule.every().day.at("09:00").do(display_namskar_everyday)

    while True:
        schedule.run_pending()
        time.sleep(20)

if __name__ == "__main__":
    main()