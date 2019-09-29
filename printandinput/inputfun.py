#s = raw_input("Enter your name: ")
#print s
#i = int(input("Enter an integer number: "))
#print i
#print type(i)

# Receiving more than one input value and looping the list
lst = [int(x) for x in raw_input("Enter three numbers separated by coma: ").split(',')]
print lst