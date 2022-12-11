d=float(input())
i=0
while d%1!=0:
    d=d*10
    i=i+1
sum=0
for n in range(10**i):
    sum=sum+1/(2*n+1)*(-1)**n
print(round(sum*4,i))