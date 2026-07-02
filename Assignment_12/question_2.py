def factors_of_given_number(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def main():
    number = int(input("Enter a number to find its factors: "))

    if number <= 0:
        print("Please enter a positive integer.")
        return 
    factors = factors_of_given_number(number)
    print(f"The factors of {number} are: {factors}")

if __name__ == "__main__":
    main()  