a, b, c = map(int, input().split())
if a>=b>=c:
    a*=2
    b*=2
    c*=2
else:
    a=abs(a)
    b=abs(b)
    c=abs(c)
print(a,b,c)
