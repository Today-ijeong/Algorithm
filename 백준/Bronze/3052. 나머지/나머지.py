b = []
for _ in range(10):
    a = int(input())
    b.append(a % 42)
print(len(set(b)))