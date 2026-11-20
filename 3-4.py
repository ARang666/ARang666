a = list(map(int, input("请输入第一个点的坐标 x y：").split()))
b = list(map(int, input("请输入第二个点的坐标 x y：").split()))

distance = abs(a[0] - b[0]) + abs(a[1] - b[1])
print(distance)
