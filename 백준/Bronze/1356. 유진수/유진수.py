def prod_each_digit_in(num_str : str):
    ret = 1
    for num_ch in num_str:
        ret *= int(num_ch)
    return ret
num_str = input()

ans = "NO"
for i in range(1, len(num_str)):
    if prod_each_digit_in(num_str[:i]) == prod_each_digit_in(num_str[i:]):
        ans = "YES"
        break

print(ans)
