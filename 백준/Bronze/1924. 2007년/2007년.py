x,y = map(int, input().split())
m = [31,28,31, 30, 31 ,30, 31, 31,30 ,31 , 30 , 31 ]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
a=0
for i in range(0,x-1):
    a+=m[i]
total_d=a+y
print(day[total_d%7])