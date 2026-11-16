# 输入任意大的自然数
s = input("请输入一个自然数：").strip()

# 逐位取出字符，转成整数后累加
total = 0
for ch in s:
    total += int(ch)

print(f"各位数字之和 = {total}")
