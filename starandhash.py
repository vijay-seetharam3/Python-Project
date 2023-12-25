s=input()
a=0
b=0
for i in s:
    if (i=="*"):
        a+=1
    elif (i=="#"):
        b+=1
    else:
        print("invalid value")
print(a-b)