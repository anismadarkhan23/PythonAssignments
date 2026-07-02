def area_of_circle(radius):
    return 3.14 * radius * radius

def main():
    radius = float(input("Enter the radius of the circle: "))
    print("The area of the circle is: ", area_of_circle(radius))

if __name__ == "__main__":
    main()