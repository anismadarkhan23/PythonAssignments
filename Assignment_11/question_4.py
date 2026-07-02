def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10
    return reversed_num

def main():
    number = int(input("Enter a number to reverse: "))
    reversed_number = reverse_number(number)
    print(f"The reversed number is: {reversed_number}")

if __name__ == "__main__":
    main()