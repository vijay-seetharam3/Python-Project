def getmaxpotency(n,c,p,b):
    def dfs(i,cost,potency):
        if cost>b:
            return -float('inf')
        if i==n:
            return potency
        fullpot=dfs(i+1,cost+c[i],potency+p[i])
        halfpot=dfs(i+1,cost+c[i]//2,potency+p[i]//2)
        skippot=dfs(i+1,cost,potency)
        return max(fullpot,halfpot,skippot)
    return max(0,dfs(0,0,0))
n=4
c=[2,4,8,16]
p=[6,20,8,7]
b=3
print(getmaxpotency(n,c,p,b))
    
