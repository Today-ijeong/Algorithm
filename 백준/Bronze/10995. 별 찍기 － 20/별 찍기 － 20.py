n = int(input())
for i in range(n):
    if n ==1:
        print("*")
    else:
        print(" "*(i%2)+"* *"+" *"*(n-2))