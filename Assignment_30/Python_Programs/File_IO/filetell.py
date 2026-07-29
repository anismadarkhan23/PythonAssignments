def main():
    try:
        f_obj = open("Demo.txt", "r")
        print("File gets opened")

        print("File offset is: ", f_obj.tell())
        print(f_obj.read(10))
        print("File offset is: ", f_obj.tell())
        
        f_obj.close()

    except FileNotFoundError as f_obj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()
