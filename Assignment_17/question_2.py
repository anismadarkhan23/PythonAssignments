# In Python's print() function, the end parameter defines what gets 
# printed at the very end of the line. By default, every time you 
# call print(), Python secretly adds a newline character (\n) to the end, 
# which pushes the cursor to the next line. When you write end = " ", 
# you are telling Python: "Hey, instead of jumping to a new line 
# when you're done printing, just print a space and stay on the same line."

def print_pattern(num):
    for i in range(num):
        for j in range(num):
            print("*", end = " ")
        print() # this will take the console to new line

def main():
    value = int(input("Enter the number to print the pattern: "))
    print_pattern(value)

if __name__ == "__main__":
    main()