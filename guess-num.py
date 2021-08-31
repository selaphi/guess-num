import random
r = random.randint(1, 100)
while True:
	guess = input('請猜1到100中的數字:')
	guess = int(guess)
	if guess == r:
		print('恭喜你，猜對了!')
		break
	elif guess > r:	
		print('要再小一點')
	elif guess < r:	
		print('要再大一點')