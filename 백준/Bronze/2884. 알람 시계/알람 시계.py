a,b = map(int,input().split())
if b>=45:
    print(a,b-45)
elif b<=44 and a!=0:
    b = 60-abs(b-45)
    print(a-1, b)
else:
    a=23
    b = 60 - abs(b - 45)
    print(a,b)