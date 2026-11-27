import random

# 猜数游戏
low = 1
high = 100
max_times = 5   # 最多猜5次
answer = random.randint(low, high)
count = 0

print("====猜数游戏====")
print(f"我生成了一个 {low} 到 {high} 的整数，你最多有 {max_times} 次猜测机会！")

while count < max_times:
    try:
        guess = int(input("请输入你猜测的数字："))
        count = count + 1
        if guess == answer:
            print(f"恭喜你猜对了！答案就是{answer}，一共猜了{count}次。")
            break
        elif guess > answer:
            print("太大了！")
        else:
            print("太小了！")
        left = max_times - count
        if left > 0:
            print(f"还剩下 {left} 次机会\n")
    except:
        print("输入非法，请输入整数！不消耗次数\n")
else:
    # 次数耗尽，没有break
    print(f"次数用完，游戏结束！正确答案是：{answer}")
