def factorial_of_number(number):
    if number == 0 or number == 1:
        return 1
    
    factorial = 1
    for i in range(number):
        factorial *= (i + 1)

    return factorial

def main():
    value = int(input("Enter the number to get the factorial: "))
    print("Factorial of given number is: ", factorial_of_number(value))

if __name__ == "__main__":
    main()