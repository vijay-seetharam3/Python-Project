r=int(input("enter: "))
unit=int(input("enter: "))
n=int(input("enter: "))
arr=list(map(int,input("enter: ").split(",")))
a=r*unit
b=0
c=0
for i in arr:
    if (b<=a):
        b+=i
        c+=1
if b>=a:
    print(c)