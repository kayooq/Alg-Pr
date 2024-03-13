from math import exp,log
n=0
while 3*n**4-730*n <5:
    n+=1
print("1)",n-1)
n=1
while exp(n) - 1000*log(n) <=10:
    n+=1
print("2)",n-1)
