i = 1
e_a = 1.0
e_n = 2.0

while (e_n - e_a > 0.00001):
    
    print(i,"\t",e_n)
    e_a = e_n
    i = i+1
    e_n = pow((1+1/i),i)