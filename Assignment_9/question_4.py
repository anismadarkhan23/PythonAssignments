get_qube = lambda number: number * number * number

def main():
    value = int(input("Enter the number: "))

    print("Qube of the number {} is: {}".format(value, get_qube(value)))

if __name__ == "__main__":
    main()