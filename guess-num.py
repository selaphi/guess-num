import random
start = input('這是個猜數字遊戲，請決定隨機數字的開始值: ')
end = input('請決定隨機數字的結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count = count + 1
	guess = input('請猜1個數字:')
	guess = int(guess)
	if guess == r:
		print('恭喜你，猜對了!')
		print('你一共猜了', count, '次')
		break
	elif guess > r:	
		print('要再小一點')
	elif guess < r:	
		print('要再大一點')
	print('你已經猜了', count, '次')
		