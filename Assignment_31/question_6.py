import schedule
import time

def main():
    schedule.every().monday.at("09:00").do(print, "Start your weekly goals")
    schedule.every().wednesday.at("17:00").do(print, "Review your weekly goals")
    schedule.every().friday.at("18:00").do(print, "Weekly work completed")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()