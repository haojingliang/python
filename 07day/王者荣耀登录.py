print('TIMI')
login = int(input('请设置登录方式1=qq,2=微信,3=账户'))
if login == 1:
	print('qq登录成功')
	hero = int(input('请选择你的英雄1=荆轲,2=李白,3=韩信'))
	if hero == 1:
		print('刺秦王!!!')
	if hero == 2:
		print('大河之剑天上来')
	if hero == 3:
		print('长枪一动，白龙吟!!!')
if login == 2:
	print('微信登录成功')
a = '123'
b = 'abc'
if login == 3:
	acc = input('请输入账号:')
	pwd = input('请输入密码:')
	if a == acc and b == b:
		print('登录成功')
	else:
		print('登录失败')


