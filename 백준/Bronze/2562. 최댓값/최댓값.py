nums = []
for i in range(0,9):
    a = int(input())
    nums.append(a)
print(max(nums))
b = int(nums.index(max(nums)))
print(b+1)