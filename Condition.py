# for finding even or odd
number=input("Number is: ")
num1=int(number)
num=num1%2
if(num==0):
    print(f"{number} is even.")
elif(num!=0):
    print(f"{number} is odd")
else:
    print("error input")





first=int(input("Enter first number"))
second=int(input("Enter second number"))

print(
    "Enter 1 for 'Addition' \nEnter 2 for 'Subtraction' \nEnter 3 for 'multiplication' \nEnter 4 for 'division':"
)
Entered_number=int(input("Enter your choice from 1 to 4:"))
if Entered_number==1:
   Entered_number=first+second
   print("Addition of {first} and {second} is :",Entered_number)
elif Entered_number==2:
    Entered_number=first-second
    print("Subtraction of {first} and {second} is:",Entered_number)
elif Entered_number==3:
    Entered_number=first*second
    print("Multiplication of {first} and {second} is:",Entered_number)
else:
    Entered_number=first/second
    print("Division of {first} and {second} is :",Entered_number)