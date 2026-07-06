def ChkNum(number):
    if number % 2 == 0:
        return True
    else:
        return False

def main():
    given_number = int(input("Enter the number to check whether it is even or odd: "))

    if given_number < 0:
        print("Error: Please enter the positive number")
    elif ChkNum(given_number):
        print("Even number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()