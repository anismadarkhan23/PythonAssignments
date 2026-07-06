def get_number_of_digits(number):
    sum = 0

    while number > 0:
        sum = sum + (number % 10)
        number = number // 10

    return sum

def main():
    given_value = int(input("Enter the number to count the digits: "))

    print(f"Number of digits in {given_value} are {get_number_of_digits(given_value)}")

if __name__ == "__main__":
    main()