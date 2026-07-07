from functools import reduce
import Marvellous_Factors

get_addition_of_factors = lambda num1, num2: num1 + num2
get_even_factors = lambda num: num % 2 == 0
get_odd_factors = lambda num: num % 2 != 0

def EvenFactor(number):
    factors = Marvellous_Factors.factors_of_given_number(number)
    
    even_factors = list(filter(get_even_factors, factors))
    print(f"Even factors of a given number are: {even_factors}")
    
    sum_of_even_factors = reduce(get_addition_of_factors, even_factors)
    print(f"Sum of even factors are: {sum_of_even_factors}")

def OddFactor(number):
    factors = Marvellous_Factors.factors_of_given_number(number)
    
    odd_factors = list(filter(get_odd_factors, factors))
    print(f"Odd factors of a given number are: {odd_factors}")
    
    sum_of_odd_factors = reduce(get_addition_of_factors, odd_factors)
    print(f"Sum of odd factors are: {sum_of_odd_factors}")

def main():
    given_number = int(input("Enter a number to find its factors: "))

    if given_number <= 0:
        print("Please enter a positive integer.")
        return 
    factors = Marvellous_Factors.factors_of_given_number(given_number)

    print("-------------------------------------------------------------")
    print(f"The factors of {given_number} are: {factors}")
    print("-------------------------------------------------------------")

    EvenFactor(given_number)
    print("-------------------------------------------------------------")
    OddFactor(given_number)
    print("-------------------------------------------------------------")

if __name__ == "__main__":
    main()  