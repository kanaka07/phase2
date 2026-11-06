def leapYear(n):
    if(n%100==0):
        if(n%400==0):
            return True
        else:
            return False
    if(n%4==0):
        return True
    else:
        return False
n=int(input("enter a year: "))
print(leapYear(n))