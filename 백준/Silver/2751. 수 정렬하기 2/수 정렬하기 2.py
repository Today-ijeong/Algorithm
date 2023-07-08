import sys
n = int(sys.stdin.readline())
arr = []
for a in range(n):
    b = int(sys.stdin.readline())
    arr.append(b)
arr = sorted(arr)
for i in range(n):
    print(arr[i])