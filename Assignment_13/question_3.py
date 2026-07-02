from functools import reduce

factors_addition = lambda number1, number2: number1 + number2

def check_perfect_number(number):
    factors = []
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)

    result = reduce(factors_addition, factors)

    return result == number

def main():
    number = int(input("Enter a number to check if it's a perfect number: "))

    if number <= 0:
        print("Please enter a positive integer.")
        return 
    is_perfect = check_perfect_number(number)
    print(f"{number} is {'a perfect number' if is_perfect else 'not a perfect number'}.")

if __name__ == "__main__":
    main()  