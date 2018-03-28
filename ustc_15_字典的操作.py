# 字典是一个无序的数据集合，输出可能是无序的
xiaomin = {"name": "小明",
           "age": 18,
           "gender": True}

# 字典取值
print(xiaomin["name"])
# 修改
xiaomin["name"] = "小花"
# 删除
xiaomin.pop("name")

# xiaomin.clear()

# 统计键值对数量
len(xiaomin)

# 合并键值对
temp_dict = {"height": 175,
             "age": 20}
# 如果被合并的字典包含已存在的键值对，会覆盖原来的键值对
xiaomin.update(temp_dict)
# 清空字典
xiaomin.clear()
print(xiaomin)
