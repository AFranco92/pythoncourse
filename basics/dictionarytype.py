# Key value pair
dict1 = {
    1 : "John",
    2 : "Bob",
    3 : "Bill"
}
print dict1

k = dict1.keys()
for i in k:
    print(i)

v = dict1.values()
for i in v:
    print(i)

print dict1[3]

del dict1[2]
print dict1