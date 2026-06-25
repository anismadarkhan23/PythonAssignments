s = "Python"
print(s)
print(id(s))
s = s + "3"
print(s)
print(id(s))

# In Python, string considered as immutable data type 
# as every time the string gets modified or created the PVM will trated as new one
# And will assign the different memory address.
# So in above code, the id will be change as at first time PVM considering it as different string
# And second time, when modification done it will be treted as different one.