print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Flore Division")
choice=input()
if choice == "1":
    num1=int(input("Enter the 1st number"))
    num2=int(input("Enter the 2nd number"))
    add=num1+num2
    print("the sum of given numbers is ", add)
elif choice=="2":
        num1=int(input("Enter the 1st number"))
        num2=int(input("Enter the 2nd number"))
        sub=num1-num2
        print("the diff between given numbers is ", sub)
elif choice=="3":
        num1=int(input("Enter the 1st number"))
        num2=int(input("Enter the 2nd number"))
        mul=num1*num2
        print("the multiplication of given numbers is ", mul)
elif choice=="4":
        num1=int(input("Enter the 1st number"))
        num2=int(input("Enter the 2nd number"))
        div=num1/num2
        print("the diff between given numbers is ", div)
elif choice=="5":
        num1=int(input("Enter the 1st number"))
        num2=int(input("Enter the 2nd number"))
        florediv=num1%num2
        print("the result is ",florediv)
else:
    print ("invalid")
