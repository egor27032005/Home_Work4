import random
k=int(input())
a=random.randint(2, 10)
print(a,end="")
print("x^",end="")
print(k,end=" + ")
while k!=0:
    k=k-1
    a=random.randint(2, 10)
    print(a,end="")
    print("x^",end="")
    print(k,end=" + ")
a=random.randint(2, 10)
print(a,end='')
print(" = 0")