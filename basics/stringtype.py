s = "You are awesome"
print s

s1 = """You are the
creator of
your destiny"""
print s1

# Printing a character of the string
print s1[0]

# Printing the string several times
print s*3

# Printing the number of items from the string
print len(s1)

# Slicing a string
print s[0:5]
print s[0:]
print s[:8]

# Slicing with steps
print s[0:9:2]

# Reverse the string
print s[::-1]

# Striping the string (take off the spaces in the beginning and in the end of it)
s2 = "       Hello   "
print s2.strip()

# Omitting the spaces placed on the left or in the right
print s2.lstrip()
print s2.rstrip()

# Finding substring in the string
print s.find("awe")

# Counting how many times an occurrence is present in the string
print s.count("a")

# Replacing a sub string to another (old, new)
print s.replace("awesome", "super")

# Uppercase, lowercase and title style of a string
print s.upper()
print s.lower()
print s.title()
