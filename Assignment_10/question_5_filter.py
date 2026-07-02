get_odd_numbers = lambda num: num % 2 != 0

def get_all_odd_numbers(number):
    number_list = get_list_till_limit_number(number)
    odd_numbers = list(filter(get_odd_numbers, number_list))
    return odd_numbers

def get_list_till_limit_number(limit_number):
    numbers = list()
    for i in range(limit_number):
        numbers.append(i + 1)
    return numbers

def main():
    value = int(input("Enter the limit number: "))
    print("All odd number till that limit number are: ", get_all_odd_numbers(value))

if __name__ == "__main__":
    main()