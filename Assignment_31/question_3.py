import os
import schedule
import time
import sys
from datetime import datetime

def scan_directory(directory_name):
    if not os.path.exists(directory_name):
        print(f"Backup Log Error: There is no such a directory with name {directory_name}")
        sys.exit(1)
    
    if not os.path.isdir(directory_name):
        print(f"Backup Log Error: {directory_name} is not a directory")
        sys.exit(1)

    scanned_directory_name = ""
    sub_directories_count = 0
    files_count = 0
    for folder_name, sub_folders, file_names in os.walk(directory_name):
        scanned_directory_name = os.path.dirname(folder_name)

        for sub_f in sub_folders:
            sub_directories_count += 1

        for f_name in file_names:
            files_count += 1 
        
    print(f"Directory scanned: {scanned_directory_name}")
    print(f"Total Sub-Directories: {sub_directories_count}")
    print(f"Total Files: {files_count}")
    print(f"Scan Time: {datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")}")

def main():
    folder_name = input("Enter the folder name to scan: ")
    schedule.every(1).minute.do(scan_directory, folder_name)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()