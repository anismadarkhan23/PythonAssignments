check_largest_number_among_three = lambda num1, num2, num3: max(num1, num2, num3) 

def main():
    value1 = int(input("Enter the first number: "))
    value2 = int(input("Enter the second number: "))
    value3 = int(input("Enter the third number: "))

    largest_number = check_largest_number_among_three(value1, value2, value3)
    print("Largest number is: ", largest_number)

if __name__ == "__main__":
    main()