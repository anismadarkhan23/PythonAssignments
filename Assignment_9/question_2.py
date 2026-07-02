def check_greater(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2

def main():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    greater_number = check_greater(value1, value2)
    print("The greater number among {} & {} is {}".format(value1, value2, greater_number))

if __name__ == "__main__":
    main()