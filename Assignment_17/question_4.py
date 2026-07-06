from functools import reduce

get_addition_of_factors = lambda num1, num2: num1 + num2

def factors_of_given_number(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def main():
    given_number = int(input("Enter a number to find its factors: "))

    if given_number <= 0:
        print("Please enter a positive integer.")
        return 
    factors = factors_of_given_number(given_number)

    print("--------------------------------------------")
    print(f"The factors of {given_number} are: {factors}")
    print("--------------------------------------------")

    sum_of_factors = reduce(get_addition_of_factors, factors)

    print(f"The addition of factors is : {sum_of_factors}")
    print("--------------------------------------------")

if __name__ == "__main__":
    main()  