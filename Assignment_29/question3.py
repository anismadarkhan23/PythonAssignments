import sys

def main():
    try:
        file_name1 = sys.argv[1]

        fh_obj9 = open(file_name1, "r")
        print(f"Contents of {file_name1} are")
        print(fh_obj9.read())
        fh_obj9.seek(0)

        file_name2 = input("Enter the file name in which conten should be copied -> ")

        fh_obj10 = open(file_name2, "w")
        fh_obj10.writelines(fh_obj9.readlines())

        fh_obj9.close()

        print("-" * 70)

        fh_obj10 = open(file_name2, "r")
        print(f"Contents of {file_name2} are")
        print(fh_obj10.read())
        fh_obj10.close()

    except IndexError:
        print("Error: File input is not given")

    except FileNotFoundError:
        print("Error: File not found...!")

if __name__ == "__main__":
    main()