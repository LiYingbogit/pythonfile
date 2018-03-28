# 定义年龄变量，年龄在0到120岁之间

age = 12
if age >= 0 and age <= 120:
    print("ok")
else:
    print("不合理")
# or 运算符
python_score = 10
c_score = 80
if python_score >= 60 or c_score >= 60:
    print("pass")
else:
    print("not pass")

# not 运算符

is_employee = True

if not is_employee:
    print("不是本公司员工")
else:
    print("是本公司员工")
