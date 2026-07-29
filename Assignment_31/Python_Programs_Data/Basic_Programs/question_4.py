def get_all_even_numbers(number):
    even_numbers = list()
    for i in range(1, number + 1):
        if i % 2 == 0:
            even_numbers.append(i)
    
    return even_numbers

def main():
    value = int(input("Enter the limit number: "))
    print("All even number till that limit number are: ", get_all_even_numbers(value))

if __name__ == "__main__":
    main()