i = 1

ha = 0.0
hn = 1.0

while (abs(hn-ha) > 0.001):
    
    print(i,"\t",hn)
    ha = hn
    i = i+1
    hn = hn + 1/i