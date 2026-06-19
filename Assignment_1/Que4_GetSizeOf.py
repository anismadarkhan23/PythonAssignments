from sys import getsizeof

no = 23
print("Size of no is: ", getsizeof(no))

str = "Hello"
print("Size of str is: ", getsizeof(str))

dict = {"name": "Anis", "age": 23}
print("Size of dict is: ", getsizeof(dict))

# why is memory size different for different data types? 
# Because different data types have different memory requirements. 
# For example, an integer requires less memory than a string 
# because an integer is a simple data type while a string is a complex data type 
# that can contain multiple characters.