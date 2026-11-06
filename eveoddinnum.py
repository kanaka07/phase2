def countnum(n):
        count=0
        while(n>0):
            r = n%10
            if r%2==1:
             count+=1
            n=n//10
n = int(input("enter a number: ")) 
print(countnum(n))   