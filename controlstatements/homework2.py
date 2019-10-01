# Error, infinity cicle

x = int(input("Enter a integer number: "))

y = 1
while y < x:
    if (y % 10 == 0):
        continue
    if y > 100:
        break
    print y
    y += 1