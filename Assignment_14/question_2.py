qube_of_number = lambda num: num * num * num

def main():
    value = int(input("Enter the number to get the qube: "))
    print("The qube of {} is {}".format(value, qube_of_number(value)))

if __name__ == "__main__":
    main()