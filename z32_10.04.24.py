max=0
znak='0'
a=int(input())
bool=a>=0
if bool == True:
    znak='+'
else:
    znak='-'
while a!=0:
    if znak=='+':
        if a<0:
            max+=1
            znak='-'
    if znak=='-':
        if a>=0:
            max+=1
            znak='+'
    a=int(input())
print(max)
