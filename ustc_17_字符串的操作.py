str1 = "hello python"

# 取指定的字符
print(str1[6])

# for循环迭代输出
for n in str1:
    print(n)

# 统计字符串的长度
print(len(str1))

# 统计某个字符出现的次数
print(str1.count("o"))

# 某个字符出现的位置
print(str1.index("llo"))

# 判断空白字符,制表符，换行符等
space_str = " "
print(space_str.isspace())

# 判断字符串是否只包含数字,以下三个方法都不能判断小数
# unicode 字符串，从上到下范围变大

num_str = "1"
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())

# 字符串文本对齐，center 方法 strip(),去除空格

poem = [
    "登黄鹤楼",
    "王之涣",
    "白日依山尽",
    "黄河入海流",
    "欲穷千里目",
    "更上一层楼"
]
# print("*"*60)
for my_poem in poem:
    print(my_poem.strip().center(10, " "))
print("*" * 60)
# 字符串的拆分和拼接
poem_str = "登黄鹤楼\n白日依山尽\t\t\n 黄河入海流\n 欲穷千里目\n 更上一层楼"
print(poem_str)
poem_list = poem_str.split()
print(" ".join(poem_list))  # 拼接
for mype in poem_list:
    print(mype.center(10))
# print(poem_list)
