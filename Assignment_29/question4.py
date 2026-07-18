import sys

def main():
    try:
        file_name1 = sys.argv[1]
        file_name2 = sys.argv[2]

        fh_obj11 = open(file_name1, "r")
        fh_obj12 = open(file_name2, "r")

        if fh_obj11.read() == fh_obj12.read():
            print("Both the file's content is same")
        else:
            print("Both the file's content is not same")
        
        fh_obj11.close()
        fh_obj12.close()

    except IndexError:
        print("Error: Invalid number of arguments. Please specify file names")
    
    except FileNotFoundError:
        print("Error: File not found")

if __name__ == "__main__":
    main()