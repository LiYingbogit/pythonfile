def test(num):
    print("在函数内部%d对应的内存地址是%d" % (num, id(num)))

    # 1.定义一个字符串变量
    result = "hello"
    print("%s的内存地址是%d" % (result, id(result)))
    # 2.将字符串变量返回
    return result


# 1. 定义一个数字变量
a = 10
# 数据的地址本质上是一个数字
print("a变量保存的地址是%d" % id(a))
# 2.调用test()函数的时候，本质上传递的是实参保存数据的引用，而不是实参保存的数据
r = test(a)
print("%s的内存地址是%d" % (r, id(r)))
