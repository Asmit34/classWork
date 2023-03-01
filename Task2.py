# Write a program that accept an integer(n) and compute the value of n+nn+nnn...
n=int(input("Enter a number:"))
a= (f"{n}")
b= (f"{n}{n}")
c= (f"{n}{n}{n}")
d= (f"{n}{n}{n}{n}")
e= (f"{n}{n}{n}{n}{n}")
sum = int(a)+int(b)+int(c)+int(d)+int(e)
print(sum)

'''Write a python program to calculate the difference betweeen the given number and 17. if the number is greater than
 17 then return twice the absolute difference
 '''

num = float(input("Enter a number: "))
#  difference between the number and 17
result=num-17
print("The difference between the number and 17 is:",result)
if num >=17:
    num= (num-17)*2
    print(num)

# write a python program to check whether a input number is prime or not
inp2 = int(input("Enter any number"))
if inp2 <= 1:
    print(f"{inp2} is not prime number")
if inp2 > 1:
    for i in range(2, inp2):
        if inp2 % i == 0:
            print(f"{inp2} is not prime number")
            break
    else:

        print(f"{inp2} is prime number")
