check_divisibility = lambda num: num % 3 == 0 and num % 5 == 0

def main():
    number_data = list()

    print("---------------------------------------------------")
    count_of_number_list = int(input("Enter the total count of number list: "))
    print("---------------------------------------------------")
    for i in range(count_of_number_list):
        number_data.append(int(input(f"Enter number {i + 1}: ")))

    print("---------------------------------------------------")
    print("Entered number list is: ", number_data)

    numbers_divisible_by_three_and_five = list(filter(check_divisibility, number_data))
    print("---------------------------------------------------")
    print("Numbers which are divisible by 3 & 5 are: ", numbers_divisible_by_three_and_five)
    print("---------------------------------------------------")

if __name__ == "__main__":
    main()