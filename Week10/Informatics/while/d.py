def is2(x):
	while x % 2 == 0:
		x //= 2
	return x == 1

if is2(int(input())):
	print('YES')
else:
	print('NO')
	