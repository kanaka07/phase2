#lst=list(map(int,input().split()))
#non_zeros=[]
#zeros=[]
#for num in lst:
 #   if(num==0):
  #      zeros.append(num)
   # else:
    #    non_zeros.append(num)
#print(non_zeros+zeros)

lst=list(map(int,input().split()))
i=-1
for ind in range(0,len(lst)):
    if(lst[ind]==0):
        i=ind
        break
if(i!=-1):
    for j in range(i+1,len(lst)):
        if lst[j]!=0:
            lst[i],lst[j]=lst[j],lst[i]
            i=i+1
print(lst)
