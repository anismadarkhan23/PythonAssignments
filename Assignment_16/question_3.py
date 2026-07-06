def Add(num1, num2):
    return num1 + num2

def main():
    given_value1 = int(input("Enter the first number: "))
    given_value2 = int(input("Enter the second number: "))

    addition = Add(given_value1, given_value2)
    print(f"Addition of {given_value1} & {given_value2} is {addition}")

if __name__ == "__main__":
    main()