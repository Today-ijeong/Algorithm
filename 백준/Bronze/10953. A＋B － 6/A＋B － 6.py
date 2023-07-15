c = []
T = int(input())
for i in range(T):
    a,b = map(str,input().split(','))

    c.append(int(a)+int(b))
print(*c,sep='\n')