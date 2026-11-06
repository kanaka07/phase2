def setbit(n,i):
    if n & (1 << i):
        print("SETBIT")
    else:
        print("NOTSET")
n=int(input('enter a number: '))
i=int(input('enter bit position: '))
setbit(n,i) 

        