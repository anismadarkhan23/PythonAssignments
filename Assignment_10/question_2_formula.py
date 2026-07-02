def calculate_first_N_numbers_using_formula(count):
    return int(count * (count + 1) / 2)

def main():
    value = int(input("Enter the count of first N numbers: "))
    result = calculate_first_N_numbers_using_formula(value)

    print("Sum of first N natural numbers are: ", result)

if __name__ == "__main__":
    main()