password = 'a123456'
i = 3
while True:
	passwordtry = input('請輸入密碼: ')
	if passwordtry == password:
		print('登入成功!')
		break
	else:
		i = i - 1
		print('密碼錯誤! 還有', i, '次機會')
		if i == 0:
			print('請過30秒再次輸入')
			break