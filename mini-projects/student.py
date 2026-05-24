def total(a,b,c):
    return a+b+c
def average(a,b,c):
    return (a+b+c)/3
def percentage(a,b,c):
    f=((a+b+c)/300)*100
    return f
def grade(a,b,c):
    per=percentage(a,b,c)
    if per>=90:
        return 'A'
    elif per>=80:
        return 'B'
    else:
        return 'C'
a=int(input("enter the marks of subject 1: "))
b=int(input("enter the marks of subject 2: "))
c=int(input("enter the marks of subject 3: "))
total=total(a,b,c)
avg=average(a,b,c)
per=percentage(a,b,c)
grd=grade(a,b,c)
print("Total marks: ",total)
print("Average marks: ",avg)        
print("Percentage: ",per)
print("Grade: ",grd)