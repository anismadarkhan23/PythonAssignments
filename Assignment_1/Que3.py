print("-" * 100)
print("Question : What does the id() function return?")
print("Answer : The id() function returns the identity of an object. \nThis is a unique integer for each object during its lifetime. \nIt represent the memory address of the variables.")
print("-" * 100)
print("Question : Is the value returned by  id() same for two variables holding the same value")
print("Answer : It depends on the data type of the variables. \nFor immutable data types like int, str, float, etc., if two variables hold the same value, they may point to the same memory address and thus have the same id(). \nFor mutable data types like list, dict, set, etc., even if two variables hold the same value, they will point to different memory addresses and thus have different id() values.")

print("Example Start")
number1 = 23
number2 = 23
print("Memory address of number1:", id(number1)) # A123
print("Memory address of number2:", id(number2)) # A123
print("-" * 100)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("Memory address of list1:", id(list1)) # B456
print("Memory address of list2:", id(list2)) # B567
print("Example End")
