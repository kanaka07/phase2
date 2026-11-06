lst=list(map(int,input().split()))
low=0
high=len(lst)-1
while(low<high):
    lst[low],lst[high]=lst[high],lst[low]
    low=low+1
    high=high-1
print(lst)