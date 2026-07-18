def main():
    try:
        file_name = input("Enter the file name: ")

        # Creating a new file with write mode
        fio_obj = open(file_name, "w") 

        # Writing into created file.
        fio_obj.write("This is Python File Handling Programming.\nLet's learn Python Machine learning with Piyush Sir.\nKeep calm & code.\nLife is very beautiful, you just need to know how to do coding - Mr. Piyush Khairnar")
        
        # Closing the file after writing completed
        fio_obj.close()

        # Opening a created file with read mode
        fio_obj = open(file_name, "r")

        # Reading the contents of created file
        print(fio_obj.read())

        # Setting offset to start so total number of lines in the file can be read
        # If not done so, the line count will be 0
        fio_obj.seek(0)

        # Displaying the total number of lines in the file
        print(f"Total number of lines in {file_name} is {len(fio_obj.readlines())}")

        # Due to above line offset is now at end of the file & hence
        # again setting offset to 0
        fio_obj.seek(0)

        # Counting the lines from the file using for loop.
        # Got to know from Python documentation
        line_count = 0
        for line in fio_obj:
            line_count += 1
        
        print(f"For Loop -> Total number of lines in {file_name} is {line_count}")

        # Closing the file after line reading operation completed
        fio_obj.close()
    
    except FileNotFoundError:
        print("Error: File is not present in current directory")

if __name__ == "__main__":
    main()