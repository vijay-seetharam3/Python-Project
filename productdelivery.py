def prodDel(O_Ids):
    lst=[]
    for i in O_Ids:
        summ=0
        for j in str(i):
            summ+=int(j)
        lst.append(summ)
    return lst
O_size=int(input())
O_Ids=list(map(int,input().split()))
result=prodDel(O_Ids)
print(" ".join([str(res) for res in result]))
