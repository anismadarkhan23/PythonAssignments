def get_factorial(number):
    product = 1
    for i in range(1, number + 1):
        product = product * i

    return product

def main():
    given_number = int(input("Enter number to get factorial: "))

    factorial = get_factorial(given_number)

    print(f"Factorial of {given_number} is {factorial}")

if __name__ == "__main__":
    main()