a=int(input("enter first number: "))
b=int(input("enter the second number "))
print("enter you operation 1,2,3,4,5")
print("1 for addition\n 2 for subtraction\n 3 for division\n 4 for multiplication\n ")
c=int(input("enter your choice"))
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mul(a,b):
    return a%b
if c==1:
    print("the sum is ",add(a,b))
elif c==2:
    print("the difference is ",sub(a,b))    
elif c==3:
    print("the division is ",div(a,b))
elif c==4:
    print("the multiplication is ",mul(a,b))
else:
    print("invalid input")
6