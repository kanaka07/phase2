num=(int(input("enter a number: ")))
count=0
for i in range (1,num+1):
    if(num%i==0):
        count=count+1
    print(i,end=" ")
print(count)