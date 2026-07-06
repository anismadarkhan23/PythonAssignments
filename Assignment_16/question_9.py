def get_first_ten_even_numbers(num):
    i = 1
    while i <= num:
        print(i * 2)
        i += 1

def main():
    get_first_ten_even_numbers(int(input("Enter number: ")))

if __name__ == "__main__":
    main()