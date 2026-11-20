import math

lst = list(map(int, input("请输入若干整数（空格分隔）：").split()))

result = math.prod(lst)    # 等价于把列表元素全部相乘，空列表返回1
print(result)
