# Get total number of words in the file

def main():
    try:
        file_name = input("Enter file name -> ")

        fh_obj2 = open(file_name, "w")
        fh_obj2.write("Anis Madarkhan, Hadapsar, Pune, Maharashtra, 411028")
        fh_obj2.close()

        fh_obj2 = open(file_name, "r")

        word_count = 0  
        for line in fh_obj2:
            for chr in line:
                if chr == ' ':
                    word_count += 1
        fh_obj2.close()

        print("Total number of words in the file:", word_count)
    
    except FileNotFoundError:
         print("Error: File not found...!")

if __name__ == "__main__":
    main()