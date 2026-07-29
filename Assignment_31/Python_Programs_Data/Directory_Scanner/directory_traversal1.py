import os

def main():
    for folder_name, sub_folder, file_name in os.walk("Marvellous"):
        print(folder_name)

if __name__ == "__main__":
    main()