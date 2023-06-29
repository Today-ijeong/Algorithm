X = int(input())
N = int(input())
a = 0
for i in range(N):
    b,c = map(int,input().split())
    a+= b*c
if (a == X):
    print("Yes")
else:
    print("No")