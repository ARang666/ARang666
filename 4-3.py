s = input("请输入字符串：")
count_dict = {}

for ch in s:
    if ch in count_dict:
        count_dict[ch] += 1
    else:
        count_dict[ch] = 1

# 找最大值
max_char = max(count_dict, key=count_dict.get)
max_times = count_dict[max_char]
print(f"出现次数最多的字符：{max_char}，次数：{max_times}")
