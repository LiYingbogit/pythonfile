def measure():
    """测量温度和湿度"""
    print("开始测量：")
    temp = 33
    wetness = 13
    print("当前的温度是：%d" % temp)
    print("当前的湿度是%d" % wetness)
    print("测试结束")

    # 元组可以包含多个数据，因此可以使用元组让函数一次返回多个值
    # 如果函数返回的类型是元组，小括号可以省略
    # return (temp,wetness)
    return temp, wetness


result = measure()
print(result)

# 需要单独的处理温度和湿度
# gl_temp = result[0]
# gl_wetness = result[1] 
# print(gl_temp)
# print(gl_wetness)
gl_temp, gl_wetness = measure()  # 注意此处变量的个数应该和元组的个数相同
print(gl_temp)
print(gl_wetness)
