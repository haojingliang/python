price = int(input("请输入身价"))
facevalue = int(input("请输入颜值分"))
height = float(input("请输入身高"))
if height > 180 and price > 1000000 and facevalue > 99:
	print("高富帅")
elif price > 1000000 and facevalue > 99:
	print("富帅")
elif facevalue > 99:
	print("帅")
elif height <= 160 and price <= 100 and facevalue <= 60:
	print("矮穷矬")

