import sys

def main():
    try:
        file_name = sys.argv[1]
        word_to_be_search = sys.argv[2]

        fh_obj13 = open(file_name, "r")

        string_ocuurences = 0
        for line in fh_obj13:
            for word in line.split():
                if word == word_to_be_search:
                    string_ocuurences += 1
            
        print(f"The word '{word_to_be_search}' occurs {string_ocuurences} times in {file_name}")    

        fh_obj13.close()

    except IndexError:
        print("Error: Invalid number of arguments. Missing argument file name or string ")

    except FileNotFoundError:
        print("Error: File not found...!")


if __name__ == "__main__":
    main()