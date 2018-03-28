# 连续打印小星星
row = 1
col = 1
while row <= 5:
    while col <= 5:
        print("*" * col)
        col += 1
    row += 1
# end的用法
row1 = 1
while row1 <= 5:
    col1 = 1
    while col1 <= row1:
        print("*", end="")  # 不要换行
        col1 += 1
    # print("*")
    print("")  # 输出换行
    row1 += 1

# 9*9乘法口诀表
row2 = 1
while row2 <= 9:
    col2 = 1
    while col2 <= row2:
        print("%2d * %2d = %2d" % (col2, row2, col2 * row2), end="\t")
        col2 += 1
    print("")
    row2 += 1

print("hello\"hello")
