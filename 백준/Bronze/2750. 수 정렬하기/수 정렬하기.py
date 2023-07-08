n = int(input())
arr_ = []
for a in range(n):
    b = int(input())
    arr_.append(b)
for i in range(n-1):
    min_idx = i
    for j in range(i+1, n):
        if arr_[min_idx]>arr_[j]:
            min_idx = j
    arr_[i],arr_[min_idx] = arr_[min_idx],arr_[i]
for p in range(n):
    print(arr_[p])