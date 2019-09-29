# A bytearray can be assigned values through the index or indexing can be performed (not slicing and repetition)
# But on the bytes we cannot assign any values and no slicing or repetition is allowed

lst = [20, 30, 40, 234]
b = bytes(lst)
print type(b)
b1 = bytearray(lst)
print type(b1)
