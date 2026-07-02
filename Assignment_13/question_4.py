def display_binary_equivalent(number):
    if number < 0:
        print("Please enter a non-negative integer.")
        return

    binary_equivalent = f"{number:b}"
    return binary_equivalent

def main():
    number = int(input("Enter a non-negative integer: "))
    result = display_binary_equivalent(number)
    print(f"The binary equivalent of {number} is: {result}")

if __name__ == "__main__":
    main()