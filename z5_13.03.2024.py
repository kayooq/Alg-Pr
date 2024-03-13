k = 1
sum=0
d =(-1)**(k+1)*(1/(2*k-1))
while abs(d) >= 0.001:
    sum+=d
    d = ((-1)**(k+1))*(1/(2*k-1)) 
    k+=1
print(sum)
