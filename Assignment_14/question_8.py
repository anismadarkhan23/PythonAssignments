sum_of_two_numbers = lambda num1, num2: num1 + num2

def main():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    print(f"Addition of {value1} & {value2} is {sum_of_two_numbers(value1, value2)}")

if __name__ == "__main__":
    main()