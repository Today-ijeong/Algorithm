c = []
while True:
    try:
        a,b = map(int,input().split())
        if (a!=0 and b !=0):
            c.append(a + b)
        else:
            break
    except:
            break

print(*c,sep='\n')