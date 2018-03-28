# break和continue
i = 0
while i < 10:
    if i == 3:
        # 对循环计数进行修改，否则进入死循环
        i = i + 1
        continue
        # break

    print(i)
    i += 1
print("over")
