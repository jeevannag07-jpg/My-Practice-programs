def largest(num1,num2):
    if num1>num2:
        return num1
    elif num1<num2:
        return num2
    else:
        return "both are equal"
a=int(input("enter your first number:"))
b=int(input("enter the second number: "))
resullt=largest(a,b)
print(resullt)