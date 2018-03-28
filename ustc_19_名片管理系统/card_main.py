
while True:
    #  TODO（小明） 显示系统菜单项目
    # print("*" * 80)
    # print("欢迎进入名片管理系统")
    # print("1.新建名片\n2.显示全部\n3.查询名片\n\n0.退出系统")
    # print("*" * 80)
    action = input("请选择操作功能：")

    print("您输入的操作是【%s】" % action)
    # 1.2.3对名片的操作
    if action in ["1", "2", "3"]:
        # 新增名片
        if action == "1":
            pass
        # 显示全部
        elif action == "2":
            pass
        # 查询名片
        elif action == "3":
            pass
        # pass

    elif action == "0":
        # pass
        # 如果在开发程序时，不希望立刻编写代码，可以通过pass关键字，表示一个占位符，能够保证程序的代码结构正确
        print("欢迎再次进入名片管理系统")
        break

    else:
        print("您输入的不正确，请重新选择")
