b = []
c = 0
N = int(input())
a = list(map(int,input()))
b = a
for i in range(N):
    c+=b[i]
print(c)