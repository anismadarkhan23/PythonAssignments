import threading
import time
from functools import reduce
import Marvellous_Factors

get_addition_of_factors = lambda num1, num2: num1 + num2
get_even_factors = lambda num: num % 2 == 0
get_odd_factors = lambda num: num % 2 != 0

def EvenFactor(number):
    print("------------------------ Start of EvenFactor ------------------------")
    print(f"----------------------- TID : {threading.get_ident()} -----------------------")
    
    factors = Marvellous_Factors.factors_of_given_number(number)
    
    even_factors = list(filter(get_even_factors, factors))
    print(f"Even factors of a given number are: {even_factors}")
    
    sum_of_even_factors = reduce(get_addition_of_factors, even_factors)
    print(f"Sum of even factors are: {sum_of_even_factors}")
    print("---------------------------------------------------------------------")

def OddFactor(number):
    print("------------------------ Start of OddFactor -------------------------")
    print(f"----------------------- TID : {threading.get_ident()} -----------------------")
    factors = Marvellous_Factors.factors_of_given_number(number)
    
    odd_factors = list(filter(get_odd_factors, factors))
    print(f"Odd factors of a given number are: {odd_factors}")
    
    sum_of_odd_factors = reduce(get_addition_of_factors, odd_factors)
    print(f"Sum of odd factors are: {sum_of_odd_factors}")
    print("---------------------------------------------------------------------")

def main():
    print("--------------------------- Start of main ---------------------------")
    print(f"----------------------- TID : {threading.get_ident()} -----------------------")
    given_number = int(input("Enter a number to find its factors: "))
    
    if given_number <= 0:
        print("Please enter a positive integer.")
        print("--------------------------- Exit from main --------------------------")
        return 
    
    start_time = time.perf_counter()

    even_factor_tObj = threading.Thread(target = EvenFactor, args = (given_number, )) 
    odd_factor_tObj = threading.Thread(target = OddFactor, args = (given_number, )) 

    even_factor_tObj.start()
    odd_factor_tObj.start()

    even_factor_tObj.join()
    odd_factor_tObj.join()

    end_time = time.perf_counter()
    print(f"Time required to perform the both threads is {end_time - start_time:.4f} seconds")
    print("--------------------------- Exit from main --------------------------")

if __name__ == "__main__":
    main()  