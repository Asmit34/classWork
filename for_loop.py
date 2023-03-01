# for <variable> in <sequence> :    (sequence=list,tuple,string)

for i in [1, 2, 3]:
    print(i, end=' ')  # printing in same line

for i in (1, 2, 3):  # for using tuple
    print(end='\n')
    print(i + 5, end=' ')

print(end='\n')  # for using string
for i in "hello":
    print(i, end=' ')
print(end='\n')

count = 0
count2 = 0
for i in "hello":  # to count the number of vowels using for loop
    if i in "aeiou":
        count = count + 1
    else:
        count2 = count2 + 1
print(f"Number of vowels is {count}")
print(f"Number of consonant is {count2}")

for i in [1, 2, 3]:  # else also doesnot execute if break is used
    print(i)
    if i == 2:
        break
else:
    print("none")

num = int(input("enter the number: "))  # checking number prime or not using for and if
for i in range(2, num):
    if num % i == 0:
        print(f"The number {num} is not prime.")
        break
else:
    print(f"The number {num} is prime.")

for j in range(1, 101):  # printing prime number upto 100
    if j > 1:
        for i in range(2, j):
            if j % i == 0:
                break
        else:
            print(j, end=' ')

print(end='\n')

result = [i for i in range(1, 101) if i % 2 == 0]
print(result)