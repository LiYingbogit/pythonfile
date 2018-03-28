#
import random

player = int(input("请输入你要出的拳（1）石头/（2）剪刀/（3）布："))

computer = random.randint(1, 3)
print("玩家出的是%d，电脑出的是%d" % (player, computer))
# if (()
#   or()
#   or()):阅读更加方便
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("玩家战胜电脑")
elif ((player == 1 and computer == 3)
      or (player == 2 and computer == 1)
      or (player == 3 and computer == 2)):

    print("电脑战胜玩家")
else:
    print("玩家和电脑平局")
# 平局更好写，player == computer
# elif player == computer:
#   print("玩家和电脑平局")
# else:
#   print("电脑战胜玩家")
