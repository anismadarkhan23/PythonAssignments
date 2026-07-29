import schedule
from datetime import datetime
import time

def create_entry_in_txt_file_for_every_five_minutes(file_name):
    print("Current date and time are logged in the file: ", file_name)
    fio_obj = open(file_name, "a+")
    fio_obj.write(f"Task executed at: {datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")}\n")
    fio_obj.close()

def main():
    schedule.every(5).minutes.do(create_entry_in_txt_file_for_every_five_minutes, "Marvellous.txt")

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()