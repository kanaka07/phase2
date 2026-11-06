def checkPrime(num):
    count=0
    for i in range (1,num+1):
        if(num%i==0):
            count=count+1
    if count==2:
        return True
    else:
        return False
n=int(input("enter a number: "))
prime_count=0
for num in range (2,n+1):
    if(checkPrime(num)==True):
        prime_count=prime_count+1
print(prime_count)
    