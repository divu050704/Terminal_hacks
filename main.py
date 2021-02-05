import os
c = 'Y'
while c == 'Y':
	print('What do you want to open')
	print('0.\t Exit')
	print('1.\t Image')
	print('2.\t PDF')
	ch = int(input('Enter your choice:\t'))
	if ch == 0:
		exit()
	if ch == 1:
		os.system('python3 open-images.py')
	if ch == 2:
		os.system('python3 open-pdf.py')
	c = input('Do you want to continue(Y/n):\t')
