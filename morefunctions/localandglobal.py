x = 123 # global variable

def display():
    x = 678 # local variable
    print x
    print globals()['x']

print x

# assign function to a variable
z = display
z()