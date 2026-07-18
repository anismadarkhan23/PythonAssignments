def main():
    try:
        file_name, word_to_be_search = input("Enter file name & word -> ").split()

        fh_obj6 = open(file_name, "r")

        for line in fh_obj6:
            if line.split().__contains__(word_to_be_search):
                print(f"{word_to_be_search} is found in {file_name}")
            else:
                print(f"{word_to_be_search} is not found in {file_name}")

        fh_obj6.close()

    except FileNotFoundError:
        print("Error: File not found...!")

if __name__ == "__main__":
    main()