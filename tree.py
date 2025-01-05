a=list(map(int,input().split()))
mxlst=[]
for i in range(len(a)+1):
    for j in range(i+1,len(a)+1):
        chck=a[i:j]
        flag=0
        for k in range(len(chck)-1):
            if chck[k] > chck[k+1]:
                flag=1 
        if len(mxlst) < len(chck) and flag==0:
            mxlst.append(chck)
print(len(max(mxlst)),sum(max(mxlst)))

#Optimized version
a = list(map(int, input().split()))
max_len = 0
max_sum = 0
start = 0
for i in range(1, len(a)):
    if a[i] < a[i-1]:
        start = i
    else:
        curr_len = i - start + 1
        curr_sum = sum(a[start:i+1])
        if curr_len > max_len or (curr_len == max_len and curr_sum > max_sum):
            max_len = curr_len
            max_sum = curr_sum
print(max_len, max_sum)
