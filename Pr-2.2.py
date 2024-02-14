x = int(input())
y = int(input())
if x >= y:
    max = x
else:
    max = y
if x <= y:
    min = x
else:
    min = y
print("1) z =", (min + 0.5)/(1+max**2))
if x >= 0:
    print("2) z =",max)
else:
    print("2) z =", min)
if y >= 0:
    print("3) z =",min)
else:
    if x**2 >= y**2:
        max = x
    else:
        min = y
    print("3) z =", max)
