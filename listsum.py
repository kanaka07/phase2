#lst=[4,5,6,7]
#print(sum(lst))
lst = list(map(int,input().split()))
Sum=0
Sum2=0
for num in lst:
    Sum=Sum+num
print(Sum)

print("---------------------")
for num in range(len(lst)):
    Sum2=Sum2+lst[num]
print(Sum)


