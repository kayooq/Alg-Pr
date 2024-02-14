a = int(input("введите а "))
b = int(input("введите b "))
if a%2 == 0 and b%2 == 0:
    print("оба четные")
if a%2 != 0 and b%2 != 0:
    print('оба нечетные')
if a%2 == 0 and b%2 != 0:
    print("a - четное, b - нечетное")
if b%2 == 0 and a%2 != 0:
    print("a - нечетное, b - четное")
