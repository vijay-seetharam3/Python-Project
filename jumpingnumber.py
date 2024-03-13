a=input()
b=len(a)
flag=0
for i in range(b-1):
 	res=abs(int(a[i])-int(a[i+1]))
    if(res!=1):
        flag=1
        break
	if flag==0:
    	print("yes")
	else:
    	print("no")
