def get_sequence_till_entered_number(number):
    sequence = list()
    for i in range(1, number + 1):
        sequence.append(i)
    return sequence 

def main():
    value = int(input("Enter the limit number: "))
    print("That many numbers starting from 1 are: ", get_sequence_till_entered_number(value))

if __name__ == "__main__":
    main()