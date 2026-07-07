get_power_of_two = lambda num: num ** 2

def main():
    given_number = int(input("Enter number: "))
    
    print(f"Power of two of {given_number} is {get_power_of_two(given_number)}")

if __name__ == "__main__":
    main()
