# Sets dont allow duplicate elements, indexing, order, slicing, repetition...
s = {10, 20, 30, "XYZ", 10, 10, 20}
print s

s.update([88, 99])
print s

s.remove(30)
print s

# Froze a set. A frozen set doesn't allow update and remove methods
f = frozenset(s)