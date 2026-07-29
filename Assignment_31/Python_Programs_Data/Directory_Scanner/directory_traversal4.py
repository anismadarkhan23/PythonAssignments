import os

def main():
    for folder_name, sub_folder, file_name in os.walk("Marvellous"):
        for f_name in file_name:
            print("File name is: ", f_name)

if __name__ == "__main__":
    main()