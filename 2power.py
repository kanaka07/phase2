def power(n):
 if n > 0 and (n & (n - 1)) == 0:
    print("Power of 2")
 else:
    print("Not a Power of 2")
n=int(input('enter a num '))
power(n)
 