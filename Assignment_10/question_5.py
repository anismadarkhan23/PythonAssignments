def get_all_odd_numbers(number):
    odd_numbers = list()
    for i in range(1, number + 1):
        if i % 2 != 0:
            odd_numbers.append(i)
    
    return odd_numbers

def main():
    value = int(input("Enter the limit number: "))
    print("All odd number till that limit number are: ", get_all_odd_numbers(value))

if __name__ == "__main__":
    main()