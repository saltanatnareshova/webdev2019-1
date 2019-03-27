def end_other(a, b):
  	a = a.lower()
  	b = b.lower()
  	return a == b[-len(a):] or b == a[-len(b):]