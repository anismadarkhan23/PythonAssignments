check_odd = lambda num: num % 2 != 0

def main():
    value = int(input("Enter number to check whether it is odd or not: "))
    
    print(check_odd(value))

if __name__ == "__main__":
    main()