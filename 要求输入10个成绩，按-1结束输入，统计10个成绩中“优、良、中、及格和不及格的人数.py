# 1.输入成绩，最多10个，输入-1结束，统计各等级人数
you = 0
liang = 0
zhong = 0
jige = 0
bujige = 0
n = 0

while n < 10:
    score = float(input("请输入成绩（输入-1结束）："))
    if score == -1:
        break
    if score < 0 or score > 100:
        print("成绩无效，请重新输入！")
        continue
    n += 1
    if score >= 90:
        you += 1
    elif score >= 80:
        liang += 1
    elif score >= 70:
        zhong += 1
    elif score >= 60:
        jige += 1
    else:
        bujige += 1

print("====统计结果====")
print(f"优：{you}人")
print(f"良：{liang}人")
print(f"中：{zhong}人")
print(f"及格：{jige}人")
print(f"不及格：{bujige}人")
