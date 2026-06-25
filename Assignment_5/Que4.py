ba = bytearray([65, 66, 67])
print(ba)
print("----------------------")
ba[0] = 97
print(ba)

# This is allowed because bytearray is mutable version of bytes data type
# And due to this we can modify the data.
# As small a hex value is 97 the output will be bytearray(b, 'aBC')