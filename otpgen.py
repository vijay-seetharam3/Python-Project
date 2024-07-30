def orderOTP(O_Id):
    OTP=1
    for i in str(O_Id):
        OTP*=int(i)
    return OTP
O_Id=int(input())
result=orderOTP(O_Id)
print(result)
