a, b, c =map(int,input().split()) 
d = (a+b)%c
e = ((a%c) +(b%c))%c
f = (a*b)%c
g = ((a%c)*(b%c))%c
print(d)
print(e)
print(f)
print(g)