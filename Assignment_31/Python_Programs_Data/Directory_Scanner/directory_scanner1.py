import os
import sys

def directory_scanner(directory_path):
    print(f"Files from the directory {directory_path} are")
    for folder_name, sub_folder, file_name in os.walk(directory_path):
        for f_name in file_name:
            print(f_name)

def main():
    BORDER = "-" * 70
    print(BORDER)
    print(" Marvellous Automation Script ")
    print(BORDER)
    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This automation script is used to travel the directory\n"
                  "For better usage please check --u or --U flag")
        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Please execute the script as 'python FileName.py directory_name'\n"
                  "Directory name should be absolute path")
        else:
            directory_scanner(sys.argv[1])

    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")

    print(BORDER)
    print(" Thank you for using Marvellous Automation Script ")
    print(BORDER)

if __name__ == "__main__":
    main()