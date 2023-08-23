import sys

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst.append(list(map(int,input().split())))
lst.sort()
for i in lst:
    print(*i)