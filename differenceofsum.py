def differenceofsum(n,m):
    a=0
    b=0
    for i in range(1,m+1):
        if(i%n!=0):
            a+=i
        else:
            b+=i
    return a-b
n=int(input("enter: "))
m=int(input("enter: "))
print(differenceofsum(n,m))