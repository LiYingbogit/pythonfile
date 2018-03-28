# 列表的操作
name_list = ["小明", "大飞", "小红", "小红"]
# 取值取索引
print(name_list[2])
print(name_list.index("大飞"))
# 修改
name_list[1] = "大大飞"
# 增加
name_list.append("小花")
# 删除
name_list.remove("小明")
# 插入
name_list.insert(1, "小梅")
# 扩展
temp_list = ["dafei", "daet"]
name_list.extend(temp_list)
# pop默认可以把最后一个数据删除
name_list.pop()
# pop可以指定索引数据删除
name_list.pop(1)

# clear整个列表删除
# name_list.clear()
list_len = len(name_list)
print("列表中包含%d个元素" % list_len)

# 统计数据的次数
count = name_list.count("小红")
print("小红出现的次数%d" % count)

print(name_list)
# help(list)
