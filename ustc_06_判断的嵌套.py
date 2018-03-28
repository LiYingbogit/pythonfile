# if语句的嵌套

has_ticket = True
knief_length = 30

if has_ticket:
    print("允许进入安检")
    if knief_length >= 20:
        print("刀长%d,不允许上车" % knief_length)
    else:
        print("允许上车")
else:
    print("不允许进入安检")
