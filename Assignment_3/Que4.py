def demo_function():
    print("Inside demo function")

def main():
    ret = demo_function()
    print("Default return value is: ",ret) 

if __name__ == "__main__":
    main()

# Output
# Inside demo function
# Default return value is:  None 
# As there is no return statement specified in the function 
# the compiler will predict the data type as None by default.