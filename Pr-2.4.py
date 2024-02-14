a = int(input())
b = int(input())
c = int(input())
maxABC = a
minABC = a
if b > maxABC:
    maxABC = b
if c > maxABC:
    maxABC = c
if b < minABC:
    minABC = b
if c < minABC:
    minABC = c
print("P =", (maxABC+minABC)/2)
