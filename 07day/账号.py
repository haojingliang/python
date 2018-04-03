sacc ='12345'
spwd = 'abc'

account = input('请输入账号')
pwd = input('请输入密码')
if sacc != account:
	print('账号错误')
	if spwd != pwd:
		print('密码错误')
if account == sacc and pwd == spwd:
	print('登录成功')
