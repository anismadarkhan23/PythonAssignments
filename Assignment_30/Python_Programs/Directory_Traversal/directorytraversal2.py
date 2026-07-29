import os

def main():
    for folder_name, sub_folder, file_name in os.walk("Marvellous"):
        print("Folder name: ", folder_name)
        
        for sub_f in sub_folder:
            print("Sub-Folder name is: ", sub_f)

if __name__ == "__main__":
    main()