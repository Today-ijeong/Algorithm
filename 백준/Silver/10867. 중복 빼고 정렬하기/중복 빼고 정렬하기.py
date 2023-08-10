n = int(input())
nums=0
sort_num = []
nums =list(set(map(int,input().split())))
nums.sort()
print(*nums)