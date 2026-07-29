import os
import sys
import time
import schedule

BORDER = "-" * 70

def delete_all_empty_files(directory_name):
    global BORDER

    empty_files = detect_all_empty_files(directory_name)

    time_stamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    log_file_name = "DeletedFiles_%s.log"%(time_stamp)

    destination_path = os.path.abspath(os.path.join(directory_name, "..", "Deleted_Files_Log_Data/"))
    os.makedirs(os.path.join(destination_path, "DeletedFilesLog_%s"%(time_stamp)), exist_ok = True)
    log_folder_path = os.path.join(destination_path, "DeletedFilesLog_%s"%(time_stamp))
    log_file_path = os.path.join(log_folder_path, log_file_name)

    f_obj = open(log_file_path, "w")

    f_obj.write(BORDER + "\n")
    f_obj.write(" Delete Empty Files Automation Script \n")
    f_obj.write(BORDER + "\n")
    f_obj.write(" Emplt Files from the directory are: \n")
    f_obj.write(BORDER + "\n")

    for empty_f in empty_files:
        f_obj.write(empty_f+" : "+str(os.path.getsize(empty_f))+" bytes\n")
        os.remove(empty_f)

    f_obj.write(BORDER + "\n")
    f_obj.write("Total empty files found & deleted : "+str(len((empty_files)))+"\n")

    f_obj.write(BORDER + "\n")
    f_obj.write(f"Log file got created at {time_stamp}\n")
    f_obj.write(BORDER + "\n")

    f_obj.close()
    print("Log File gets created with name: ", log_file_name)

def detect_all_empty_files(directory_name):
    if not os.path.exists(directory_name):
            print(f"Delete Empty File Automation Script Error: There is no such a directory with name {directory_name}")
            return
        
    if not os.path.isdir(directory_name):
        print(f"Delete Empty File Automation Script Error: {directory_name} is not a directory")

    emply_files_paths = list()

    for folder_name, sub_folder, file_name in os.walk(directory_name):
        for f_name in file_name:
            file_path = os.path.join(folder_name, f_name)
            if os.path.getsize(file_path) == 0:
                emply_files_paths.append(os.path.abspath(file_path))

    return emply_files_paths

def main():
    global BORDER
    print(BORDER)
    print(" Marvellous Automation Script ")
    print(BORDER)
    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This automation script is used to delete the empty files from directory\n"
                  "For better usage please check --u or --U flag")
        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print(f"Please execute the script as 'python {sys.argv[0]} directory_name'\n"
                  "Directory name should be absolute path")
        else:
            schedule.every(1).hour.do(delete_all_empty_files, sys.argv[1])

            while True:
                schedule.run_pending()
                time.sleep(1)

    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")

    print(BORDER)
    print(" Thank you for using Marvellous Automation Script ")
    print(BORDER)

if __name__ == "__main__":
    main()