a=int(input("enter the number of elements you want to store"))
list=[]
for i in range(a):
    p=int(input("enter the element"))
    list.append(p)
print(list)
even_list=[]
for i in list:
    if i%2==0:
        even_list.append(i)
print(even_list)