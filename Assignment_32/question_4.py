import sys
import schedule
import time
import os
from datetime import datetime 
import shutil
import mimetypes

BORDER = "-" * 70

def copy_text_files(dir_name):
    global BORDER

    time_stamp = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p").replace(" ", "_").replace("-", "_").replace(":", "_")
    log_file_name = "TextFile_%s.Log"%(time_stamp)
    
    if not os.path.exists(dir_name):
        print(f"Backup Log Error: There is no such a directory with name {dir_name}")
        return
    
    if not os.path.isdir(dir_name):
        print(f"Backup Log Error: {dir_name} is not a directory")
        return

    script_paths = list()
    destination_path = os.path.abspath(os.path.join(dir_name, "..", "..", "Assignment_31/"))

    for folder_name, sub_folder, file_names in os.walk(dir_name):
        for f_name in file_names:
            mime_type, _ = mimetypes.guess_type(f_name)
            if mime_type == "text/plain":
                script_rel_path = os.path.join(folder_name, f_name)
                script_paths.append(os.path.abspath(script_rel_path))

    if len(script_paths) == 0:
        print(f"Backup Log Error: There are no such files in the directory {dir_name} to backup")
        return
    
    os.makedirs(os.path.join(destination_path, "CopiedTextFilesLog_%s"%(time_stamp)), exist_ok = True)

    log_folder_path = os.path.join(destination_path, "CopiedTextFilesLog_%s"%(time_stamp))
    log_file_path = os.path.join(log_folder_path, log_file_name)

    fio_obj = open(log_file_path, "a+")
    fio_obj.write(BORDER + "\n")
    fio_obj.write("Data Backup Automation Script\n")
    fio_obj.write(BORDER + "\n")
    fio_obj.write(f"Below Text Files Copied Successfully At {datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}\n")

    for file_path in script_paths:
        shutil.copy(file_path, log_folder_path)
        fio_obj.write(file_path+"\n")
    
    fio_obj.write(BORDER + "\n")
    fio_obj.close() 

    print(f"Text file gets copied successfully at {datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}")

def main():
    global BORDER

    print(BORDER)
    print(" Data Backup Automation Script ")
    print(BORDER)
    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This automation script is used to copy the text files from\n"
                  "a specified location to another specified location\n"
                  "For better usage please check --u or --U flag")
        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print(f"Please execute the script as 'python {sys.argv[0]} directory_name'\n"
                  "Directory name should be absolute path")
        else:
            schedule.every(10).minutes.do(copy_text_files, sys.argv[1])

            while True:
                schedule.run_pending()
                time.sleep(1)

    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")
    
    print(BORDER)
    print(" Thank you for using Data Backup Automation Script ")
    print(BORDER)

if __name__ == "__main__":
    main()