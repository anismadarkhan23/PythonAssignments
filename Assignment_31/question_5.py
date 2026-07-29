import os
import schedule
import time
import sys
from datetime import datetime

def get_files_count_from_directory(directory_name):
    if not os.path.exists(directory_name):
        print(f"Backup Log Error: There is no such a directory with name {directory_name}")
        sys.exit(1)
    
    if not os.path.isdir(directory_name):
        print(f"Backup Log Error: {directory_name} is not a directory")
        sys.exit(1)

    files_count = 0
    for folder_name, sub_folders, file_names in os.walk(directory_name):
        for f_name in file_names:
            files_count += 1 

    fio_obj = open("DirectoryCountLog.txt", "a+")
    fio_obj.write("-" * 150 +"\n")
    fio_obj.writelines(f"Directory Path: {os.path.abspath(directory_name)}\n"
                       f"Total Files: {files_count}\n"
                       f"Scan Time: {datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")}\n")
    fio_obj.write("-" * 150 +"\n")
    print("Directory Count Log Generated...!")

def main():
    folder_name = input("Enter the folder name to scan: ")
    schedule.every(5).minutes.do(get_files_count_from_directory, folder_name)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()