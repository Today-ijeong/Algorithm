n = int(input())
null = n-1
for i in range(1,n+1):
    print(" "*null + "*"*(2*i-1))
    null-=1