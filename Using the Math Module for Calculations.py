import math
a=float(input("Enter the first number: "))
if a>0:
    square=math.sqrt(a)
    logarithm =math.log(a)
    sine=math.sin(a)
    print("Square Root: ",square)
    print("Logarithm: ",logarithm)
    print("Sine: ",sine)
else:
    print("Enter a number greater than 0")
