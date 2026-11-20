lstA = list(map(int, input("请输入列表lstA的元素（空格分隔）：").split()))
lstB = list(map(int, input("请输入列表lstB的元素（空格分隔）：").split()))

n = min(len(lstA), len(lstB))          # 取两个列表中较短的个数
d = dict(zip(lstA[:n], lstB[:n]))      # 以lstA为键、lstB为值

print(d)
