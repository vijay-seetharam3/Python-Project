it = int(input())
result=[]
for i in range(it):
    s = int(input())
    a = list(map(int,input().split()))
    fq = dict()
    for i in a:
        if i not in fq:
            cnt = a.count(i)
            fq[i] = cnt
    vs=[sorted(fq.values())[-1]]
    res=[]
    for i,j in fq.items():
        if j in vs:
            res.append(i)
    result.append(str(min(res)))
print('\n'.join(result))