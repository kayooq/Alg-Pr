x = int(input())
y = int(input())
if x >= y:
    max = x
    min = y
else:
    max = y
    min = x
print("1) z =", (min + 0.5)/(1+max**2))
if x >= 0:
    print("2) z =",max)
else:
    print("2) z =", min)
if y >= 0:
    print("3) z =",min)
else:
    if x**2 >= y**2:
        max = x**2
    else:
        min = y**2
    print("3) z =", max)
