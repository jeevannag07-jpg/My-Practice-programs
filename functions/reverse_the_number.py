def reverse_number(n):
    reverse=0
    while n>0:
        digit=n%10
        reverse=reverse*10+digit
        n=n//10
    return reverse
n=int(input("enter the number:"))
result=reverse_number(n)
print(result)