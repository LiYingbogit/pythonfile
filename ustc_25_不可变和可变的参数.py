def demo1(num, num_list):

    num = 100
    num_list = [1, 2, 3]
    print("demo1运行后的结果是%d" % num)
    print(num_list)
    return num, num_list


gl_num = 99
gl_list = [4, 5, 6]
print(demo1(gl_num, gl_list))
print(gl_num)
print(gl_list)
