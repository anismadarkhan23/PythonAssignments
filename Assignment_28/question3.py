def main():
    try:
        file_name = input("Enter the file name to be created -> ")

        fh_obj3 = open(file_name, "w")
        fh_obj3.writelines("India is my country\n"
                           "All Indian are my brothers & sisters\n"
                           "Bharat mata ki Jai...\n"
                           "Jai Hind...\n"
                           "Vande Mataram")
        fh_obj3.close()

        fh_obj3 = open(file_name, "r")
        print(f"Displaying each line of {file_name} one by one")
        print(fh_obj3.read())
        fh_obj3.close()

    except FileNotFoundError:
         print("Error: File not found...!")

if __name__ == "__main__":
    main()