import os

def main():
    try:
        file_name = input("Enter the file name -> ")

        fh_obj7 = open(file_name, "w")

        if os.path.exists(file_name):
            print(f"{file_name} is exist in current directory.")
        else:
            print(f"{file_name} is not exist in current directory.")
    
    except FileNotFoundError:
        print("Error : File not found...!")

if __name__ == "__main__":
    main()