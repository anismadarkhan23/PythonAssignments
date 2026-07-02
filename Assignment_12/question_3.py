def arithmetic_operations(number1, number2):
    summation = number1 + number2
    difference = number1 - number2
    product = number1 * number2
    quotient = number1 / number2 if number2 != 0 else None
    return summation, difference, product, quotient

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    summation, difference, product, quotient = arithmetic_operations(num1, num2)

    print(f"Addition of {num1} and {num2}: {summation}")
    print(f"Difference of {num1} and {num2}: {difference}")
    print(f"Product of {num1} and {num2}: {product}")
    if quotient is not None:
        print(f"Quotient of {num1} and {num2}: {quotient}")
    else:
        print("Quotient: Division by zero is not allowed.")

if __name__ == "__main__":
    main()