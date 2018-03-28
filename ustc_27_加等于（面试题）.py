def demo(num, num_list):
    print("函数开始")
    num += num
    # 在python中，列表变量调用+=，不会做相加在赋值的操作，
    # num_list = num_list + num_list
    # 本质上是执行列表变量的extend方法，
    # num_list += num_list 等价于下面的代码
    num_list.extend(num_list)
    print(num)
    print(num_list)
    print("函数调用结束")
    return num, num_list


gl_list = [1, 2, 3]
gl_num = 10
print(demo(gl_num, gl_list))
print(gl_num)
print(gl_list)
