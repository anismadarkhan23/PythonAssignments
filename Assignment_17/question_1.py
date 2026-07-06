from Arithmetic import Add, Sub, Mult, Div

def main():
    print("------------------------------------------------")
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))
    print("------------------------------------------------")

    sum = Add(value1, value2)
    print(f"Summation of {value1} & {value2} is {sum}")
    print("------------------------------------------------")

    diff = Sub(value1, value2)
    print(f"Difference of {value1} & {value2} is {diff}")
    print("------------------------------------------------")

    product = Mult(value1, value2)
    print(f"Product of {value1} & {value2} is {product}")
    print("------------------------------------------------")

    quotient = Div(value1, value2)
    print(f"Quotient of {value1} & {value2} is {quotient}")
    print("------------------------------------------------")

if __name__ == "__main__":
    main()