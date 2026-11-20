lst = list(map(int, input("请输入若干整数（空格分隔）：").split()))

newLst = sorted(lst, reverse=True)    # sorted返回新列表，原列表不变

print(newLst)
