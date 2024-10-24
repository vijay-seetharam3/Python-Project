a = int(input())
b = int(input())

if len(str(a)) != len(str(b)):
    print('0')
else:
    temp1 = str(a)
    temp2 = str(b)
    tsum = 0
    for i in range(1, len(temp1) + 1):
        v1 = int(temp1[-i])
        v2 = int(temp2[-i])
        summ = v1 + v2
        if summ>10:
            tsum += summ // 10
    print(tsum)
