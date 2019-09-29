from tensorflow.lite.experimental.examples import lstm
lst = [10, 20, "Franco", -10, 30.5]
print lst
print lst[3]

# Slicing the list
print lst[3:5]

# Repeating it
print lst*4;

# Getting the length
print len(lst)

# Add element
lst.append(40)
print lst

# Remove element by its value
lst.remove("Franco")
print lst

# Remove by passing the index
del(lst[1])
print lst

# Remove all the elements of the list
#del(lst[:])
#print lst

# Getting the max and the min element
print max(lst)
print min(lst)

# Inserting an element in a particular position
lst.insert(3, 99)
print lst

# To order
lst.sort()
print lst

# To order in reverse
lst.sort(reverse=True)
print lst




