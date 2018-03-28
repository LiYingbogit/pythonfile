gl_num = 10


# 修改全局变量的值，注意在开发时，应该吧模块中的所有全局变量定义在所有函数的上方，就可以保证所有的函数都能访问到所有的全局变量
def demo1():
    global gl_num
    gl_num = 99
    print("demo1输出%d" % gl_num)


def demo2():
    num = 22
    print("demo2输出结果%d" % num)


def demo3():
    print("demo3的输出结果是%d" % gl_num)


def demo4():
    print("%d" % gl_num)
    print("%s" % title)
    print("%s" % name)


name = "xiaoming"
title = "python"
demo1()
demo2()
demo3()
demo4()
