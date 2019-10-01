maths = int(input("Enter maths marks: "))
physics = int(input("Enter physics marks: "))
chemistry = int(input("Enter chemistry marks: "))

if maths >= 35 and physics >= 35 and chemistry >= 35:
    print "You have passed the exam!"
    average = (maths+physics+chemistry)/3
    if average <= 59:
        print "You got a C."
    elif average <= 69:
        print "You got a B."
    else:
        print "You got a A."
else:
    print "You failed the exam."