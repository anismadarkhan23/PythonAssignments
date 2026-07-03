check_string_lenght = lambda word: len(word) > 5

def main():
    string_data = list()

    print("---------------------------------------------------")
    count_of_string_list = int(input("Enter the total count of string list: "))
    print("---------------------------------------------------")
    for i in range(count_of_string_list):
        string_data.append(input(f"Enter string {i + 1}: "))

    print("---------------------------------------------------")
    print("Entered string list is: ", string_data)

    filtered_strings = list(filter(check_string_lenght, string_data))
    print("---------------------------------------------------")
    print("Strings with length greater than 5: ", filtered_strings)
    print("---------------------------------------------------")

if __name__ == "__main__":
    main()