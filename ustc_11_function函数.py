# 9*9乘法口诀表
# 1.函数的定义  2.函数的调用


def multimodel():
    """ 乘法口诀表，官方给的函数注解方式"""
    row2 = 1
    while row2 <= 9:
        col2 = 1
        while col2 <= row2:
            print("%2d * %2d = %2d" % (col2, row2, col2 * row2), end="\t")
            col2 += 1
        print("")
        row2 += 1


def sayhello(name):
    """ 打招呼"""
    print("hello1%s" % name)
    print("hello2")


def sum_2_num(num1, num2):
    """计算两个数的和"""
    sum1 = num1 + num2
    print("%2d +%2d =%2d" % (num1, num2, sum1))
    return sum1


def test1():
    """函数的嵌套调用"""
    print("*" * 50)
    test2()


def test2():
    print("-" * 50)


def print_line(char, num):
    """

    :param char:
    :param num:
    :return:
    """
    print(char * num)
    # print("*" * 50)


def print_lines(char, times):
    """
    :param char:
    :param times:
    :return:
    """
    row4 = 0
    while row4 < 5:
        print_line(char, times)
        row4 += 1


name = "小明"
if __name__ == '__main__':
    multimodel()
    sayhello("小明")
    result = sum_2_num(1, 2)
    print(result)
    test1()
    print_line("$", 50)
    print_lines("&", 30)
