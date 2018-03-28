# 列表的迭代遍历
name_list = ["张三", "李四", "王五", "赵六"]

for name in name_list:
    print("他们的名字是%s" % name)

# 定义元组,元组一般保存的数据不一样

info_tuple = ("zhangsan", 18, 180)
for item in info_tuple:
    print(item)
# 格式化字符串，元组
print("姓名是%s,年龄是%d,身高是%d" % info_tuple)
# 统计计数 和索引
print(info_tuple.count("zhangsan"))
print(info_tuple.index(180))

# 元组长度
print(len(info_tuple))
# 类型
print(type(info_tuple))
print(info_tuple[1])
