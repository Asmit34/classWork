# Write a python program to calculate the distance the between the points (x1,y1) and (x2,y2).
import math
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("The distance between the points ({}, {}) and ({}, {}) is {:.2f}".format(x1, y1, x2, y2, distance))


# Write a python program to test whether a passed letter is a vowel or not
vowels="a","e","i","o","u"
a=input("Enter a input:")
if a in vowels:
    print("It is vowel")
else:
    print("It is not vowel")

# Write a python program to sum two given integer.However,if the sum is between 15 and 20, it will print 20
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))

    sum = num1 + num2

    if sum >= 15 and sum <= 20:
        print("20")
    else:
        print(sum)