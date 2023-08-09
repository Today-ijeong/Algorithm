num = []
while True:
    num.append(list(map(int, input().split())))
    if num[-1] == [0,0]:
        break
for i in range(len(num)):
    if num[i][0] > num[i][1]:
        print("Yes")
    elif num[i][0] +num[i][1] == 0:
        pass
    else :
        print("No")