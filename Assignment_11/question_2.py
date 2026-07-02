def count_digits_in_number(num):
    count = 0
    if num == 0:
        return 1
    while num > 0:
        num //= 10
        count += 1
    return count

def main():
    number = int(input("Enter a number to count its digits: "))
    digit_count = count_digits_in_number(number)
    print(f"The number of digits in {number} is: {digit_count}")

if __name__ == "__main__":
    main()