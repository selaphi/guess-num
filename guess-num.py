import random
x = input('這是個猜數字遊戲，請決定最大的數字範圍是多少: ')
x = int(x)
r = random.randint(1, x)
count = 0
while True:
	count = count + 1
	guess = input('請猜1個數字:')
	guess = int(guess)
	if guess == r:
		print('恭喜你，猜對了!')
		break
	elif guess > r:	
		print('要再小一點')
	elif guess < r:	
		print('要再大一點')
	print('你已經猜了', count, '次')
		