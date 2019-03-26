b = int(input())
a = int(input())
x = a * b
if b < 0:
	while x < 0:
		x += 109
print(x % 109)
