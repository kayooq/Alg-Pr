x = int(input())
y = int(input())
print("1) z =", (min(x,y) + 0.5)/(1+max(x,y)))
if x >= 0:
    print("2) z =",max(x,y))
else:
    print("2) z =", min(x,y))
if y >= 0:
    print("3) z =",min(x,y))
else:
    print("3) z =", max(x**2,y**2))
