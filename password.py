pwd = 'a123456'
i = 3
while i > 0:
	pwdt = input('請輸入密碼: ')
	i = i - 1
	if pwdt == pwd:
		print('登入成功!')
		break
	else:
		if i == 0:
			print('密碼錯誤! 帳號已被鎖定')
			break
		print('密碼錯誤! 還有', i, '次機會')
