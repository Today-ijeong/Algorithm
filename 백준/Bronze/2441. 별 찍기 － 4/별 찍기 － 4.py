n = int(input())

for i in range(n + 1, 0, -1):
    print("{:>{}}".format('*' * (i - 1), n))