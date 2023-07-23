generated_num = set()
natural_num = set(range(1,10001))
couns = 0
for i in range(1,10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)
couns = sorted(natural_num-generated_num)
for i in couns:
    print(i)