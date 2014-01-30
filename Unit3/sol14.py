# p14: Polygonal
from math import sqrt
n = int(raw_input('enter number: '))
x = int(sqrt(n))
if x*x < n:
	exit('Invalid input. Must be perfect square.')
if x%2 == 1:
	print int(x*(x-1)/2)
	print int(x*(x+1)/2)
else:
	print int((x-1)*x/2)
	print int(x*(x+1)/2)
