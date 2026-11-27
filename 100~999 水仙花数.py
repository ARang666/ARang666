# 2.输出100-999所有水仙花数
print("100~999之间的水仙花数：")
for i in range(100, 1000):
    bai = i // 100          # 百位
    shi = (i // 10) % 10    # 十位
    ge = i % 10             # 个位
    if bai**3 + shi**3 + ge**3 == i:
        print(i)
