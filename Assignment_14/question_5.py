check_even = lambda num: num % 2 == 0

def main():
    value = int(input("Enter number to check whether it is even or not: "))
    
    print(check_even(value))

if __name__ == "__main__":
    main()