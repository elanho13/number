import random

r = random.randint(1, 100)
x = 53
while True:
	num = input('請猜數字:')
	num = int(num)
	if num == x:
		print('猜對了!')
		break
	elif num > x:
		print('比答案大!')
	else:
		print('比答案小!')
	

