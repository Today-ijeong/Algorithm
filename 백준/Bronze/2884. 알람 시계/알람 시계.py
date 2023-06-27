h,m = map(int,input().split())

if m-45 <0 and h!=0:
    m = 60-(45-m)
    h=h-1
elif h==0 and m-45 <0 :
        h=23
        m = 60-(45-m)
elif m-45>=0:
    m = m-45
print(h,m)