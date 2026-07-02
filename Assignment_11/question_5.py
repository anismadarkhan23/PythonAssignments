def check_palindrome(number):
    original_number = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = (reversed_number * 10) + digit
        number //= 10

    return original_number == reversed_number

def main():
    number = int(input("Enter a number to check if it's a palindrome: "))
    if check_palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")

if __name__ == "__main__":
    main()