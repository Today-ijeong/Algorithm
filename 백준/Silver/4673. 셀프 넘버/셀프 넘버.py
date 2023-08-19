split_num = set()
all_num = set(range(1,10001))
cnt = 0
for i in range(1,10001):
    for j in str(i):
        i += int(j)
    split_num.add(i)
cnt = sorted(all_num-split_num)
for k in cnt:
    print(k)