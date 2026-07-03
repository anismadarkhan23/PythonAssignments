square_of_number = lambda num: num * num 

def main():
    value = int(input("Enter the number to get the square: "))
    print("Square of {} is {}".format(value, square_of_number(value)))
    pass

if __name__ == "__main__":
    main()