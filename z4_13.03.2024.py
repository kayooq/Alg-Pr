a = 0
b = 1

m = int(input())

while m >= b:
    b = a+b
    a = b-a
print("1) ",b)
a = 0
b = 1
sum = b
while b <= 1000:
    b = a + b
    a = b - a
    sum += b
print("2)",sum)
