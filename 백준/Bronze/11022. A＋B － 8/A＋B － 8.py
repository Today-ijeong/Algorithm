c = []
d = []
e = []
t = int(input())
for i in range(0,t):
    a,b= list(map(int,input().split()))
    c.append(a+b)
    d.append(a)
    e.append(b)
for j in range(1,t+1):
    print("Case #%d:"%j,d[j-1],"+",e[j-1],"=",c[j-1])