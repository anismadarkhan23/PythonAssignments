def check_divisibility(number):
    if number < 0:
        return "Please enter the positive number"
    elif number % 3 == 0 and number % 5 == 0:
        return str(number) + " is divisible by 3 & 5"
    elif number % 3 == 0:
        return str(number) + " is divisible by 3 only"
    elif number % 5 == 0:
        return str(number) + " is divisible by 5 only"
    else:
        return str(number) + " is not divisible by 3 & 5"

def main():
    value = int(input("Enter the number to check the divisibility: "))

    print(check_divisibility(value))

if __name__ == "__main__":
    main()