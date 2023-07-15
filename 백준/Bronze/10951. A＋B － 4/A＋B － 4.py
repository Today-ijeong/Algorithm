c = []
while True:
    try:
        a,b = map(int,input().split())
        c.append(a+b)
    except:
        break
print(*c,sep='\n')