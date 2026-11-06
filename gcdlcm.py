from math import gcd
num1 = int(input())
num2 = int(input())
gcd_result=gcd(num1,num2)
lcm_result=gcd(num1*num2)//gcd_result
print(lcm_result)