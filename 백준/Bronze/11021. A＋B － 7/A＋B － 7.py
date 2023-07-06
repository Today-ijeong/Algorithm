c = []
t = int(input())
for i in range(0,t):
    a,b= map(int,input().split())
    c.append(a+b)
for j in range(1,t+1):
    print("Case #%d:"%j,c[j-1])