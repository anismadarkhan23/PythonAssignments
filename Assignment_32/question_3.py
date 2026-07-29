import sys
import os
import schedule
import time

def display_file_contents(file_name):
    if not os.path.exists(file_name):
        print("Can not open the file as it is not exist")
        sys.exit(1)
    elif not os.path.isfile(file_name):
        print("Path is a directory, not a file")
        sys.exit(1)
    elif not os.access(file_name, os.R_OK):
        print("Permission Denied: Can not read the file")
        sys.exit(1)
    else:
        fio_obj = open(file_name, "r")
        print(fio_obj.read())
        print("-"*40)
        # fio_obj.seek(0)
        fio_obj.close()

def main():
    schedule.every(10).seconds.do(display_file_contents, "File.txt")
            
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

# "FileDemo.txt"
# If you specifically need to check permissions before attempting an operation, 
# use os.access() with permission flags like os.R_OK (read), os.W_OK (write), 
# or os.X_OK (execute).