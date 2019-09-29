# Ranges start in 0 to -value passed as parameter-
r = range(5)
for i in r:
	print i

# Passing two parameters to set the start and the finish
r2 = range(1, 6)
for j in r2:
	print j

# Passing three, the third parameter is the number of steps
r3 = range(1, 15, 3)
for k in r3:
	print k
