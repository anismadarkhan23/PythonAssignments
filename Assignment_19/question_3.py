from functools import reduce

get_filtered_data = lambda num: num >= 70 and num <= 90
get_mapped_data = lambda num: num + 10
get_reduced_data = lambda num1, num2: num1 * num2

def store_given_value_in_list(number):
    number_list = list()
    for num in range(1, number + 1):
        number_list.append(int(input(f"Enter number {num}: ")))
    
    return number_list

def main():
    print("--------------------------------------------------------------")
    limit_number = int(input("Enter the limit number: "))

    given_list = store_given_value_in_list(limit_number)

    print("--------------------------------------------------------------")
    print(f"Given list is {given_list}")
    print("--------------------------------------------------------------")

    filtered_data = list(filter(get_filtered_data, given_list))
    print(f"Filtered data which contains elements between 70 & 90 is: {filtered_data}")
    print("--------------------------------------------------------------")

    mapped_data = list(map(get_mapped_data, filtered_data))
    print(f"Mapped data with elements increased by 10 is: {mapped_data}")
    print("--------------------------------------------------------------")

    reduced_data = reduce(get_reduced_data, mapped_data)
    print(f"Reduced data with multiplication of all numbers is: {reduced_data}")
    print("------------------------------------------------")

if __name__ == "__main__":
    main()