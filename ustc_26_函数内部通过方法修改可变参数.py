# 如果传递的参数是可变类型，在函数内部，使用方法修改了数据的内容，同样会影响到外部的数据
def demo(num_list):
    print("函数内部代码")
    # 使用方法修改列表内容，也会影响到外部数据
    num_list.append(4)
    print(num_list)
    print("函数执行完成")
    return num_list


num_list = [1, 2, 3]
print(demo(num_list))  # 调用demo函数
print(num_list)  # 此时全局变量也被修改了


