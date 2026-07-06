def get_number_of_digits(number):
    count = 0

    while number > 0:
        number = number // 10
        count += 1

    return count

def main():
    given_value = int(input("Enter the number to count the digits: "))

    print(f"Number of digits in {given_value} are {get_number_of_digits(given_value)}")

if __name__ == "__main__":
    main()