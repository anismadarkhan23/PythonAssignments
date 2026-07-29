get_even_numbers = lambda num: num % 2 == 0

def get_all_even_numbers(number):
    number_list = get_list_till_limit_number(number)
    even_numbers = list(filter(get_even_numbers, number_list))
    return even_numbers

def get_list_till_limit_number(limit_number):
    numbers = list()
    for i in range(limit_number):
        numbers.append(i + 1)
    return numbers

def main():
    value = int(input("Enter the limit number: "))
    print("All even number till that limit number are: ", get_all_even_numbers(value))

if __name__ == "__main__":
    main()