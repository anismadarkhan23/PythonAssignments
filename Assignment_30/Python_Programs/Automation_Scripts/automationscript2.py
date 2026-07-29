import sys

def main():
    if len(sys.argv) == 2:
        directory_name = sys.argv[1]
        print(f"Directory name is {directory_name}")
    else:
        print("Invalid number of arguments")

    
if __name__ == "__main__":
    main()