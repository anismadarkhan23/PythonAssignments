get_square = lambda number: number * number

def main():
    value = int(input("Enter the number: "))

    print("Square of the number {} is: {}".format(value, get_square(value)))

if __name__ == "__main__":
    main()