import time
import schedule
import os
from datetime import datetime

def get_file_size_details(file_name):
    fio_obj = open("FileSizeLog.txt", "a+")
    fio_obj.write("-" * 50 +"\n")
    fio_obj.writelines(f"File Path: {os.path.abspath(file_name)}\n"
                       f"File Size: {os.path.getsize(file_name)} bytes\n"
                       f"Creation Date & Time: {datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")}\n")
    fio_obj.write("-" * 50 +"\n")
    print("Size checked. Please check the logs")

def main():
    schedule.every(30).seconds.do(get_file_size_details, "FileDemo.txt")
        
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()