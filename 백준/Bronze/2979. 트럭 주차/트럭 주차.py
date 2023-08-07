cnt = [0]*100
a,b,c = list(map(int,input().split()))
for _ in range(3):
    start, end = map(int,input().split())
    for i in range(start,end):
        cnt[i]+=1
print(cnt.count(1)*a +cnt.count(2)*b*2+cnt.count(3)*c*3)