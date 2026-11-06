
def linerarSearch(lst):
    for num in range (0,len(lst)):
        if(lst[num]==target):
            return True 
            #print(true)
            #flag
    return False #writing this outside the loop prints false after checking all the elements
lst=list(map(int,input().split()))
target=int(input("enter target element: "))
print(linerarSearch(lst))

#direct method: lst.sort()