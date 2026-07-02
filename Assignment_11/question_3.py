def sum_of_digits_in_number(num):
    total = 0
    while num > 0:
        quotient = num % 10
        num = num // 10
        total += quotient
    return total

def main():
    number = int(input("Enter a number to find the sum of its digits: "))
    digit_sum = sum_of_digits_in_number(number)
    print(f"The sum of digits in {number} is: {digit_sum}")

if __name__ == "__main__":
    main()