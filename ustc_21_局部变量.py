# 局部变量就是临时保存一下函数内部需要使用的数据
gl_num = 11


def demo1():
    num = 10
    print("在demo1函数内部的变量是%d" % num)
    num = 20
    print("在demo1函数内部修改后的变量是%d" % num)


def demo2():
    # pass
    print(gl_num)


demo1()
demo2()
