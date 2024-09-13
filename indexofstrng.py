"""a = input()
b = input()
for i in range(len(a)):
    if b[0] == a[i]:
        if b == a[i:(len(a)-len(b))]:
            print(a.index(a[i]))
        else:
            print(-1)


n = int(input())
arr = list(map(int, input().split()))
r = int(input())

rotated_arr = arr[-r:] + arr[:-r]

print(''.join(map(str, rotated_arr)))


n=int(input())
a=list(map(int,input().split()))
summ=sum(a)
s=0
for i in range(len(a)):
    s+=a[i]
    summ-=a[i]
    if s==summ:
        print("yes")
        print("lp =",a[:i+1])
        print("rp =",a[len(a[:i+1]):])
        break
else:
    print(-1)
"""
f = open("demofile2.txt", "x")
f.close()
