# Set (Unordered,changeble,Unindixed,No duplicate)

b={}
print(type(b))
a={2,"HI","Bye",True,2,4}
print(type(a))
print(a)
# Set opeartion
a.add("apple")
print(a)

a.add("apple")
print(a)

a.update({6,7})
print(a)

s1={1,2,3,4}
s1.discard(4)
print(s1)
s1.remove(3)
print(s1)
s1.pop()
print(s1)
s1.clear()
print(s1)

# Union, intersection and difference

A={1,2,3,4}
B={3,4,5,6}

A.union(B)

A.intersection(B)

A.difference(B) #A-b

B.difference(A)   #B-A

District1={"Dang","Chitwan","Pokhara","Kathmandu"}
District2={"Chitwan","Lalitpur","Pokhara","Surkhet"}
District3=District1.symmetric_difference(District2)
print(District3)

# Set Comphrenhension

num=[]
for i in range(100):
    if i%3==0:
        num.append(i)
print(num)                    # it take more line and space so we use comprehension

a={i for i in range(100) if i % 3 ==0}
print(a)

{i for i in range(11) if i%2==0 }

numbers = {i if i % 2 == 0 else -i for i in range(10)}
print(numbers)

{i for i in range(10) if i%3==0}