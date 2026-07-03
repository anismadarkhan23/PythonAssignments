get_maximum = lambda num1, num2: num1 > num2 

def main():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    if get_maximum(value1, value2):
        print("Maximum number is ",value1)
    else:
        print("Maximum number is ",value2)

if __name__ == "__main__":
    main()