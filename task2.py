import math
n=(float(input("enter a number :")))
def operation(n):
    sqrt=math.sqrt(n)
    print("the square root of",n,"is:",sqrt)
    sin=math.sin(n)
    print("the sine of",n,"is:",sin)
    logg=math.log(n)
    print("the logarithm of",n,"is:",logg)

operation(n)