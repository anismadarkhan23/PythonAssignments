import schedule
from datetime import datetime
import time

def create_log_file():
    time_stamp = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p").replace(" ", "_").replace("-", "_").replace(":", "_")
    log_file_name = "MarvellousLog%s.txt"%(time_stamp)

    fio_obj = open(log_file_name, "w")
    fio_obj.write("-" * 50 +"\n")
    fio_obj.writelines("Log file created successfully\n"
                       f"Creattion Time: {datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")}\n")
    fio_obj.write("-" * 50 +"\n")
    fio_obj.close()
    print("Log file generated...!")

def main():
    schedule.every(10).minutes.do(create_log_file)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()