text = input("请输入一组数字（空格分隔）：").strip()
nums = [float(x) for x in text.split()]

if not nums:
    print("列表为空，无法计算")
else:
    print("原列表：", nums)
    print("排序后：", sorted(nums))   # 内置函数 sorted，返回新列表
    print("最大值：", max(nums))      # 内置函数 max
    print("均值：", sum(nums) / len(nums))  # sum 与 len 相除