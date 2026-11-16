def read_set(prompt):
    text = input(prompt).strip()
    return set(text.split()) if text else set()

A = read_set("请输入集合A（元素用空格分隔）：")
B = read_set("请输入集合B（元素用空格分隔）：")

print("A =", sorted(A))
print("B =", sorted(B))
print("交集 A∩B =", sorted(A & B))
print("并集 A∪B =", sorted(A | B))
print("差集 A-B =", sorted(A - B))
print("差集 B-A =", sorted(B - A))