n = int(input())
if n % 2 == 1:
    print('Weird')
elif n == 2 or n == 4:
    print('Not Weird')
elif n <= 20:
    print('Weird')
else:
    print('Not Weird')
