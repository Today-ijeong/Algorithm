n = int(input())
fib_1 = 0
fib_2 = 1
fib_curr = 0
if n == 0:
    print(fib_1)
elif n == 1:
    print(fib_2)
else:
    for i in range(2,n+1):
        fib_curr = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_curr
    print(fib_curr)