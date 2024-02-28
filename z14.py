x,y,m,n = map(int, input().split())
if x - y < m % n:
    x+=1
print(x)
