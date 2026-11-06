def armstrong(num):
    original=num
    num2=num
    count=0
    while(num>0):
        num=num//10
        count+=1
    sum=0
    while(num2>0):
        rem=num2%10
        sum=sum+(rem**count)
        num2=num2//10
    if (sum==original):
        return True
    else:
        return False
num=int(input("enter a num: "))
print(armstrong(num))