n = int(input())
a = [int(x) for x in input().split()]

ok = False

for i in range(1, n):
	if a[i] * a[i - 1] > 0:
		print('YES')
		ok = True
		break

if not ok:
	print('NO')
	 