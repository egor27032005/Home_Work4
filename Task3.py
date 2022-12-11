print("введите длину массива: ")
x=int(input())
mas = []
for i in range(x):
   print("Введите элемент массива: ")
   mas.append(int(input()))
mas.sort()
print(mas)
list=[]
for i in range(x-1):
    if mas[i]!=mas[i+1] and mas[i]!=mas[i-1]:
        list.append(mas[i])
if mas[x-1]!=mas[x-2]:
    list.append(mas[x-1])
print(list)