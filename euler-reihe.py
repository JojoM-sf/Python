import math

e = math.exp(1)
print(e)

i = 0
S = 1.0

while (abs(e-S) > 0.000000000000001):
    
    print(i,"\t",S)
    i = i + 1
    S = S + 1/math.factorial(i)