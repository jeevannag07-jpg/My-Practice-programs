a=int(input("enter the number of values you want to store"))
list=[]
for i in range(a):
    p=int(input("enter you element"))
    list.append(p)
print(list)
smallest=list[0]
for i in list:
    if smallest>i:
        smallest=i
print(smallest)