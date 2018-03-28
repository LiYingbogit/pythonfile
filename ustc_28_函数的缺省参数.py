gl_list = [3, 5, 2]
# 默认按照升序排序
# gl_list.sort()
# 如果需要执行降序排序，指定reverse 的值为True
gl_list.sort(reverse=True)
print(gl_list)


# 1.缺省参数，需要使用最常见的值作为默认值
def print_gender(name, gender=True):
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s是%s" % (name, gender_text))


name1 = "小明"
print_gender(name1)

name2 = "小梅"
print_gender(name2, gender=False)
