lst = list(map(int,input().split()))
count=0
count2=0
for num in lst:
    if num%2==1:
        count=count+1
print(count)
print("---------------------")
for num in range(len(lst)):
    if lst[num]%2==1:
        count2=count2+1
print(count2)
   

