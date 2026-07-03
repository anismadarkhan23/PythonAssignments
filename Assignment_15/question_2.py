get_even_numbers = lambda num: num % 2 == 0

def main():
    number_data = list()

    print("---------------------------------------------------")
    count_of_number_list = int(input("Enter the total count of number list: "))
    print("---------------------------------------------------")
    for i in range(count_of_number_list):
        number_data.append(int(input(f"Enter number {i + 1}: ")))

    print("---------------------------------------------------")
    print("Entered number list is: ", number_data)

    even_numbers = list(filter(get_even_numbers, number_data))
    print("---------------------------------------------------")
    print("Even number list is: ", even_numbers)
    print("---------------------------------------------------")

if __name__ == "__main__":
    main()