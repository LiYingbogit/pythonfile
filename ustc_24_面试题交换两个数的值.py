a = 3
b = 4

# 交换两个数的值
# 1.常规方法
# c = a
# a = b
# b = c
#
# print(a)
# print(b)

# 2.不增加变量的个数（经典的面试题）
# a = a + b
# b = a - b
# a = a - b
#
# print(a)
# print(b)


# 3.python 专门的写法
# a, b = (b, a)#提示等号的右边是一个元组
a, b = b, a

print(a)
print(b)
