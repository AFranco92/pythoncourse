"""Note: if you wanna put one single element to the tuple, you must put a comma after the element,
if not, it will be considered like the type of the element and not as a tuple."""
tpl = (40, 50, 40, "XYZ")
print tpl

print tpl[3]
print tpl*3

# Count how many times a value is present
print tpl.count(40)

# Get the index of a value
print tpl.index("XYZ")

# Convert a list into a tuple
lst = [67, 34, "XYZ"]
tpl1 = tuple(lst)
print tpl1