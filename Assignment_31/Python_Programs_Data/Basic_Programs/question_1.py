def multiplication_table(number):
    table = list()
    for i in range(1, 11):
        table.append(number * i)
    
    return table

def main():
    value = int(input("Enter the number to generate the multiplication table: "))
    result = multiplication_table(value)
    print("Multiplication table of {} is {}".format(value, result))

if __name__ == "__main__":
    main()