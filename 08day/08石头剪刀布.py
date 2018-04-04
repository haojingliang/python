import random
i = 0
w = int(input('请输入次数'))
while i <= w:
	player = int(input("请输入1=石头2=剪刀3=布"))
	computer = random.randint(1,3)
	if (player == 3 and computer == 1) or (player == 2 and computer == 3) or (player == 1 and computer == 2):
		print('玩家赢')
	elif player == computer:
		print('平局')
	else:
		print('电脑赢')
	i+=1
