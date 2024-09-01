arr=list(map(int,input().split()))
num=int(input())
diff=int(input())
cnt=0
for i in arr:
    if i==0 and abs(i-num)<diff:
        print(-1)
    if abs(i-num)<=diff:
        cnt+=1
if cnt:
    print(cnt)
else:
    print(0)

    
        
