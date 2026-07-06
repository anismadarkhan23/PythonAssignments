def display_stars_based_on_input(number):
    for i in range(number):
        print("*")

def main():
    given_number = int(input("Enter the number: "))
    display_stars_based_on_input(given_number)

if __name__ == "__main__":
    main()