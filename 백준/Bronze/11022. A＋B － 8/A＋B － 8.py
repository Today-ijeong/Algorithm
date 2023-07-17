T = int(input())
c = []
d = []
e = []
for i in range(T):
    a,b = list(map(int,input().split()))
    c.append(a+b)
    d.append(a)
    e.append(b)
for j in range(T):
    print("Case","#"+str(j+1)+":",d[j],"+",e[j],"=",c[j])