import random
c = random.randint(1,100)
i = 1
while i <= 10:
	a = (int(input('请输入数字'))
	if a > c:
		print('猜大啦')
	elif a < c:
		print('猜小了')
	else:
		print('猜中了')
		break
	i+=1
