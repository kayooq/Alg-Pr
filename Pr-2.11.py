x, y = map(float, input().split())
if x**2+y**2<=1:
    print("а) принадлежит")
else:
    print("a) не принадлежит")
if 0.25<=x**2+y**2<=1:
    print("б) принадлежит")
else:
    print("б) не принадлежит")
if x<=1 and y<=1:
    print("в) принадлежит")
else:
    print("в) не принадлежит")
