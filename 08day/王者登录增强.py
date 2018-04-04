a = '123456'
b = '000000'
i = 1
while True:
	acc = input('请输入账号')
	pwd = input('请输入密码')
	if acc == a and pwd == b:
		hero = int(input('请输入英雄名字1=w,2=e,3=h'))
		if hero == 1:
			print('niutou')
		elif hero == 2:
			print('jingke')
		elif hero == 3:
			print('libai')
		break
	else:
		print('error%d'%i)
		i+=1
		if i == 4:
			print('已锁')
			break
