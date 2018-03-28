# while 的操作
i = 0
result = 0
while i <= 100:
    if i % 2 == 0:
        result += i
        print(i)
        break
    # 1.希望执行的代码
    # print("hello")
    # 2.处理计数器
    i += 1

print(result)
