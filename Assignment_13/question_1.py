def area_of_rectangle(length, width):
    return length * width

def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    print("The area of the rectangle is: ", area_of_rectangle(length, width))

if __name__ == "__main__":  
    main()