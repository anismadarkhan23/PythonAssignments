check_largest_number_among_three_x = lambda data: max(data) 

def check_largest_number_among_three(data):
    largest_num = 0

    for num in data:
        if num > largest_num:
            largest_num = num
    
    return largest_num

def main():
    data_list = list()

    value = int(input("Enter the limit number to accept:"))

    for i in range(value):
        data_list.append(int(input(f"Enter number {i + 1}: ")))

    largest_number = check_largest_number_among_three(data_list)
    print("Largest number using def is: ", largest_number)

    largest_number = check_largest_number_among_three_x(data_list)
    print("Largest number using lambda is: ", largest_number)

if __name__ == "__main__":
    main()