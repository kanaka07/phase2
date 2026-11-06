lst=list(map(int,input().split()))
largest=float("-inf")
for num in lst:
    if(num>largest):
        largest=num
print(largest)

smallest= lst[0] #float("inf")
for num in range(0,len(lst)):
    if(lst[num]<smallest):
        smallest=lst[num]
print(smallest)
#-------------------------------------Second Largest---------------------------------------
s1=set(lst)
lst1=list(s1)
lst1.sort()
print(lst[-2])
print(lst[1])