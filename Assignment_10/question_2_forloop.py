def sum_of_first_n_numbers(number):
    total = 0
    for i in range(number):
        total += (i + 1)

    return total

def main():
    value = int(input("Enter the first N natural number count: "))
    result = sum_of_first_n_numbers(value)

    print("Sum of first N natural numbers are: ", result)

if __name__ == "__main__":
    main()