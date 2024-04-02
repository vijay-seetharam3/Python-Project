import sys
n=int(sys.argv[1])
marks=list(map(int,sys.argv[2:n]))
k=int(sys.argv[n+2])
e=int(sys.argv[n+3])
s=sorted(marks)[:k]
summ=sum(s)
if summ>e:
    print("ext")
else:
    print("nor")