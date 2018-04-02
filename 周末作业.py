p = float(input("请输入价格"))
w =float(input("亲输入重量"))
money = (p*w)
print(money)

print("*"*50)

name = input("请输入姓名:")
company = input("请输入公司:")
title = input("请输入职位:")
phone = input("请输入电话:")
email = input("请输入邮箱:")

print("*"*50)
print(company)
print()
print("%s(%s)"%(name,title))
print()
print("电话: %s"%phone)
print("邮箱: %s"%email)

print("*"*50)

print("一年=%s秒"%(60*60*24*365))
print("一公里=%s毫米"%(1000*1000))

print("*"*50)

print("*"*50)
x = 2
print(x**2)
print(6*(x/7))
print(6*(5*x))


print("*"*50)

name = input("请输入姓名")
gender = input("请输入性别")
phone = input("请输入电话号码")
addr = input("请输入家庭住址")
email = input("请输入电子邮件")
print("姓名%s\n性别%s\n电话号码%s\n家庭住址%s\n电子邮件%s\n"%(name,gender,phone,addr,email))

print("*"*50)

account = input("请输入您的账号")
password = input("请输入您的密码")
nick_name = input("请输入您的姓名")
money = 20000#原有的存款
need_money = input("请输入您要提取的金额")
sum = (money - int(need_money))
print("账号:%s\n密码******\n姓名:%s\n原有存款为%d\n取款的金额%s\n剩余%d"%(account,nick_name,money,need_money,sum))


print("*"*50)

name = input("请输入商品名称")
price = float(input("请输入商品价格"))
weight = float(input("请输入商品重量"))
money = price * weight
print(money)


print("*"*50)
size = input("请输入房屋大小")
mianji = float(input("请输入房屋面积"))
city = input("请输入所处城市")
weizhi = input("请输入详细位置")
price = float(input("请输入价格"))
guwen = input("请输入购房顾问")

print("房屋大小%s\n房屋面积%s\n所处城市%s\n详细位置%s\n价格%s\n顾问%s\n"%(size,mianji,city,weizhi,price,guwen))
