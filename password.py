x = 3
while x > 0 :
	password = input('請輸入密碼:')
	if password == 'a123456':
		print('登入成功')
		break
	else:
		x = x - 1
		print('密碼錯誤剩餘次數' , x)
	