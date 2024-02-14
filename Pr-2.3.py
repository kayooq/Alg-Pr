x = int(input())
y = int(input())
z = int(input())
minXYZ = x
if x >= z:
    maxXZ = x
else:
    maxXZ = z
if y < minXYZ:
    minXYZ = y
if z < minXYZ:
    minXYZ = z
print("L =", 2*maxXZ - 3*minXYZ)
