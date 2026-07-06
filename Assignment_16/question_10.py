def check_length_of_given_string(passed_string):
    count = 0
    for char in passed_string:
        count += 1
    
    return count

def check_string_length_using_len(passed_string):
    return len(passed_string)

def main():
    given_string = input("Enter the string to calculate its length: ")
    
    print("The length of given string is: ", check_length_of_given_string(given_string))
    print("The length of given string using len: ", check_string_length_using_len(given_string))

if __name__ == "__main__":
    main()