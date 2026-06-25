from sys import getsizeof

variable = input("Enter the value of the variable: ")

print("Data type of entered variable is: ", type(variable))
print("Memory address of entered variable is: ", id(variable))
print("Size in bytes of entered variable is: ", getsizeof(variable))

# Output
# Enter the value of the variable: 23
# Data type of entered variable is:  <class 'str'>
# Memory address of entered variable is:  4368532944
# Size in bytes of entered variable is:  43