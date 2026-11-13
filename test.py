# 输入三位整数
num = int(input("请输入一个三位正整数："))

# 拆分百位、十位、个位
bai = num // 100
shi = num // 10 % 10
ge = num % 10

sum_all = bai + shi + ge
print(f"各位数字之和 = {sum_all}")