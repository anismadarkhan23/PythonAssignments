import sys
from tabulate import tabulate
from proc_info import process_scanner
from psutil import Process

BORDER = "-" * 62

def is_given_process_running(processes_list, process_name):
    for process in processes_list:
        if process.get("name") == process_name:
            return True, process

    return False, None

def display_given_process_information(process_name):
    current_processes_list = process_scanner()

    status_check, process = is_given_process_running(current_processes_list, process_name)
    if status_check:
        process_list = []
        headers = ["PID", "Process Name", "Username", "Status"]    
        process_list.append([process.get("pid"), process.get("name"), process.get("username"), process.get("status")])

        print(tabulate(process_list, headers = headers, tablefmt = "grid"))

        c_proc = Process(process.get("pid"))
        c_proc.kill()
        
        print("Process Killed Successfully")
        
    else:
        print(f"{process_name} is not active or running")

def main():
    print(BORDER)
    print("----- Automation Script to display given process details ----- ")
    print(BORDER)

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This automation script is use to fetch\n"
                    "the Process Id, Process Name, Username & its status\n" 
                    "of given process name.\n")
            
        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the automation script as :\n"
                    f"python {sys.argv[0]} process_name\n"
                    "process_name : Name of the process to check its details.")
        else:
            display_given_process_information(sys.argv[1])

    else:
        print("Invalid number of arguments")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for getting more information")
    
    print(BORDER)
    print("--------- Thank you for using our automation system ----------")
    print(BORDER)

if __name__ == "__main__":
    main()