def check_divisibility_by_five(number):
    if number % 5 == 0:
        return True
    else:
        return False

def main():
    print(check_divisibility_by_five(int(input("Enter the number to check whether it is divisibile by 5 or not: "))))

if __name__ == "__main__":
    main()