def check_positive_or_negative(number):
    if number == 0:
        return "0 is neither positive or negative number. It is natural number"
    elif number > 0:
        return "Positive number"
    else:
        return "Negative number"

def main():
    given_number = int(input("Enter number to check whether it is positive or negative: "))
    print(check_positive_or_negative(given_number))

if __name__ == "__main__":
    main()