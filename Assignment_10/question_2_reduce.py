from functools import reduce

sum_of_first_natural_numbers = lambda number1, number2: number1 + number2

def calculate_sum(count):
    data = get_data(count)
    totalSum = reduce(sum_of_first_natural_numbers, data)
    return totalSum

def get_data(element_count):
    temp_list = list()
    for i in range(element_count):
        temp_list.append(i + 1)

    return temp_list

def main():
    value = int(input("Enter the count of first N numbers: "))
    result = calculate_sum(value)

    print("Sum of first N natural numbers are: ", result)

if __name__ == "__main__":
    main()