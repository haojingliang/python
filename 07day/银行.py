a = '1111'
p = '1234'
b = 10000

acc = input('请输入账号')
pwd = input('请输入密码')
if acc == a and p == pwd:
	print('可以取钱了')
	mn = int(input('请输入提取金额'))
	if mn <= b:
		print("提取金额%d,剩余金额%d"%(mn,b-mn))
	else:
		print('没钱')
else:
	print('非法账户')

