#!/usr/bin/python3
import ustc_19_名片管理系统tools
while True:
    #  TODO（小明） 显示系统菜单项目
    ustc_19_名片管理系统tools.show_menu()
    action = input("请选择操作功能：")

    print("您输入的操作是【%s】" % action)
    # 1.2.3对名片的操作
    if action in ["1", "2", "3"]:
        # 新增名片
        if action == "1":
            ustc_19_名片管理系统tools.new_card()
            # pass

        # 显示全部
        elif action == "2":
            ustc_19_名片管理系统tools.show_all()
            # pass
        # 查询名片
        elif action == "3":
            ustc_19_名片管理系统tools.search_card()
            # pass
        # pass

    elif action == "0":
        # pass
        # 如果在开发程序时，不希望立刻编写代码，可以通过pass关键字，表示一个占位符，能够保证程序的代码结构正确
        print("欢迎再次进入名片管理系统")
        break

    else:
        print("您输入的不正确，请重新选择")
