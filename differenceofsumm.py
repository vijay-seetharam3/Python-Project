n,m=map(int,input().split())
sumn=0
sumd=0
for i in range(1,m+1):
    if i%n==0:
        sumn+=i
    else:
        sumd+=i
print(sumd-sumn)
