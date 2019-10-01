primeFlag = True
x = int(input("Enter a number to know if it's prime or not: "))
for i in range(2, x-1):
    if x % i == 0:
        primeFlag = False
if primeFlag:
    print x,"is a prime number"
else:
    print x,"is not a prime number"