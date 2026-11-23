from functools import reduce

# 输入列表，里面元素是集合
lst = eval(input("请输入包含若干集合的列表："))
res = reduce(lambda a, b: a | b, lst)
print("并集：", res)
