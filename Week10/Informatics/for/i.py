import math

n = int(input())
x = int(math.sqrt(n))

ans = 0

for i in range(1, x):
	if n % i == 0:
		ans += 2

if n % x == 0:
	ans += 1

print(ans)
