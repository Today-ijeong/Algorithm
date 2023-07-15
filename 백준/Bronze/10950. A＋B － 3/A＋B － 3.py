T = int(input())
c = []
for i in range(T):
    a, b = list(map(int,input().split()))
    c.append(a+b)
print(*c,sep='\n')