import time
import schedule
from datetime import datetime

def file_details():
    time_stamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S").replace(" ", "_").replace("-", "_").replace(":", "_")
    file_name = "File_%s.txt"%(time_stamp)

    fio_obj = open(file_name, "w")
    fio_obj.write("-" * 50 +"\n")
    fio_obj.writelines(f"File name: {file_name}\n"
                       f"Creation Date: {datetime.now().strftime("%d-%m-%Y")}\n"
                       f"Creation Time: {datetime.now().strftime("%I:%M:%S %p")}\n")
    fio_obj.write("-" * 50 +"\n")

def main():
    schedule.every(1).minute.do(file_details)
        
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()