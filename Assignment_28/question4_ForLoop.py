def main():
    try:
        file_name1, file_name2 = input("Enter the file names -> ").split()

        fh_obj4 = open(file_name1, "r")
        print(f"Contents of {file_name1} are")
        print(fh_obj4.read())
        fh_obj4.seek(0)

        fh_obj5 = open(file_name2, "w")
        for line in fh_obj4:
            fh_obj5.write(line)

        fh_obj4.close()

        print("-" * 70)

        fh_obj5 = open(file_name2, "r")
        print(f"Contents of {file_name2} are")
        print(fh_obj5.read())
        fh_obj5.close()
    
    except FileNotFoundError:
        print("Error: File not found...!")

if __name__ == "__main__":
    main()