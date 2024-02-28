A,B,x,y,z = map(int, input().split())
if (x<=A and (y<=B or z<=B)) or (y<=A and (x<=B or z<=B)) or (z<=A and (y<=B or x<=B)):
    print('проходит')
else:
    print("не проходит")
