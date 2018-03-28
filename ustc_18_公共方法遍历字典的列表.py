# 完整的for循环语句
gl_num = [1, 2, 3]
for nu in gl_num:
    print(nu)
    if nu == 2:
        break
else:
    print("这句会执行吗？")

print("执行结束！")


student = [{"name": "小明"},
           {"name": "小梅"}]
find_name = "小梅"
for stu_dict in student:
    print(stu_dict)
    if stu_dict["name"] == find_name:
        print("找到了%s" % find_name)
        break
else:
    # 如果希望在搜索列表时，所有字典在检查之后，都没有发现需要搜索的目标，还希望得到一个统一提示
    print("抱歉没有找到%s" % find_name)

print("循环结束！")
