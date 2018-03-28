# 字典的遍历
xiaoming_dict = {"name": "小明",
                 "age": 17,
                 "phone": 10086}

for k in xiaoming_dict:
    print("%s : %s" % (k, xiaoming_dict[k]))
# 将多个字典放到一个列表当中

xinxi_list = [
    {"name": "张三",
     "age": 19,
     "phone": 10086},
    {"name": "李四",
     "age": 22,
     "phone": 10023}
]

# 遍历列表
for my_info in xinxi_list:
    print(my_info)

print(xinxi_list)
