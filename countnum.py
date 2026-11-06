def countnum(n):
        count=0
        while(n>0):
            n = n//10
            count+=1
        return count
n = int(input("enter a number: ")) 
print(countnum(n))   