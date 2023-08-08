h, m, s = map(int, input().split())
sec = int(input())
def divmod(divide, num):
  return (num//divide, num%divide)

add_m, s = divmod(60, s + sec)
add_h, m = divmod(60, m + add_m)
_, h = divmod(24, h + add_h)

print(h, m, s)