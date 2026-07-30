import sys
import os
import time
from proc_info import process_scanner

BORDER = "-" * 64

def log_processes_info(folder_name):
    if os.path.exists(folder_name):
        if not os.path.isdir(folder_name):
            print("Unable to proceed as folder name is existing but its not a directory.")
            sys.exit(1)
    else:
        os.mkdir(folder_name)
        print("Directory for the log file gets created successfully.")

    time_stamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    file_name = os.path.join(folder_name, "RunningProcessesInfo_%s.txt" %time_stamp)

    fio_obj = open(file_name, "w")
    
    print(f"Log file gets successfully created with name {file_name}")

    fio_obj.write(BORDER+"\n")
    fio_obj.write("----- Operating System's Current Running Processes Surveillance System ----- \n")
    fio_obj.write("Log files gets created at: "+time_stamp+"\n")
    fio_obj.write(BORDER+"\n")
    fio_obj.write("--------------------------------- System report -----------------------------\n")

    # Process Log
    process_data = process_scanner()

    killed_processes_count = 0
    
    for process in process_data:
        # if process.get("status") == "idle" and (process.get("pid") != 0 and process.get("pid") != 1):
        #     killed_processes_count += 1
        #     k_proc = psutil.Process(process.get("pid"))
        #     k_proc.kill()
        
        fio_obj.write("PID : %s\n" %process.get("pid"))
        fio_obj.write("Name : %s\n" %process.get("name"))
        fio_obj.write("Username : %s\n" %process.get("username"))
        fio_obj.write("Status : %s\n" %process.get("status"))
        fio_obj.write(BORDER+"\n")
        
    fio_obj.write(f"Total idle processes killed : {killed_processes_count}\n")
    fio_obj.write(BORDER+"\n")
    fio_obj.write("------------------------------- End of Log File -----------------------------n")
    fio_obj.write(BORDER+"\n")
    fio_obj.close()

def main():
    print(BORDER)
    print("----- Automation Script to log running processes details ----- ")
    print(BORDER)

    # --h & --u handling
    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This automation script is use to perfom\n"
                  "1 : It fetch the information of running processess.\n"
                  "2 : It gets auto scheduled periodically.\n"
                  "3 : It maintain all records into log file.\n")
            
        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the automation script as :\n"
                  f"python {sys.argv[0]} folder_name\n"
                  "folder_name : Name of folder for log file creation.")
        else:
            log_processes_info(sys.argv[1])

    else:
        print("Invalid number of arguments")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for getting more information")
    
    print(BORDER)
    print("--------- Thank you for using our automation System -----------")
    print(BORDER)

if __name__ == "__main__":
    main()