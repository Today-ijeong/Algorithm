a,b = map(int,input().split())
c = int(input())
next_m= b+c
add_h=0

if (next_m>=60):
    add_h = next_m//60
    next_m=next_m%60
a = a + add_h
a%=24
print(a,next_m)