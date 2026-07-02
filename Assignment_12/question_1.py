def check_vowel_or_consonant(element):
    if len(element) != 1 or not element.isalpha():
        return None
    if element.lower() in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False

def main():
    character = input("Enter a character to check whether it is vowel or not: ")

    if check_vowel_or_consonant(character):
        print(f"{character} is a vowel.")
    elif check_vowel_or_consonant(character) is False:
        print(f"{character} is a consonant.")
    else:
        print("Invalid input. Please enter a single alphabetic character.")
        
if __name__ == "__main__":
    main()