a=int(input("enter the how much elements you want to store"))
list=[]
for i in range(a):
    p=int(input("enter your element"))
    list.append(p)
print(list)
sum=list[0]
for i in list:
    sum=sum+1
print(sum)