n=int(input("enter a number: "))
def largedigit(n):
 largest=0
 while(n>0):
  rem=n%10
  n=n//10
  if(rem>largest):
    largest=rem
 return largest
print(largedigit(n))
      