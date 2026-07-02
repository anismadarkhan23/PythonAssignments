from math import sqrt

def check_prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
    
def main():
    value = int(input("Enter the number to check whether it is prime or not: "))

    if check_prime_number(value):
        print(f"{value} is a prime number.")
    else:
        print(f"{value} is not a prime number.")

if __name__ == "__main__":
    main()