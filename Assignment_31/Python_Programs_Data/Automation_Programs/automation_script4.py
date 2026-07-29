import sys

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This automation script is used to travel the directory\n"
                  "For better usage please check --u or --U flag")
        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Please execute the script as \n"
                  "python FileName.py directory_name\n"
                  "Directory name should be absolute path")
        else:
            directory_name = sys.argv[1]
            print(f"Directory name is {directory_name}")
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")

    
if __name__ == "__main__":
    main()