def get(number):
    sequence = list()

    for i in range(number, 0, -1):
        sequence.append(i)
    return sequence

def main():
    value = int(input("Enter the limit number: "))
    print("All numbers till that limit number are: ", get(value))

if __name__ == "__main__":
    main()