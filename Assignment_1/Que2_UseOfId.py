print("---------------------------------------------------------------------------------------------------------------------------------")
print("-------------Int Declaration------------")
a = 10
b = 10

print(id(a)) # A345
print(id(b)) # A345
print("In case of int, both a and b are pointing to the same memory address " + str(id(a)) + " because they have the same value 10.")
# In case of int, both a and b are pointing to the same memory address A345 because they have 
# the same value 10.
print("---------------------------------------------------------------------------------------------------------------------------------")
print("------------List Declaration------------")
a = [10] 
b = [10] 

print(id(a)) # C456
print(id(b)) # C567
print("In case of list, both a and b are pointing to different memory addresses " + str(id(a)) + " and " + str(id(b)) + " because list is a mutable data type and they should have different memory addresses even though they have the same value [10]. If they point to same memory address, then changing the value of one list will also change the value of the other list.")
# In case of list, both a and b are pointing to different memory addresses C456 and C567 
# because list is a mutable data type and they should have different memory addresses 
# even though they have the same value [10]. 
# If the point to same memory address, then changing the value of one list will also 
# change the value of the other list.
print("---------------------------------------------------------------------------------------------------------------------------------")