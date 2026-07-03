check_divisibility_by_five = lambda num: num % 5 == 0

def main():
    value = int(input("Enter number to check whether it is divisible by 5 or not: "))
    
    print(check_divisibility_by_five(value))

if __name__ == "__main__":
    main()