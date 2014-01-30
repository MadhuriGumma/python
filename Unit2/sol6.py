# prob6: Einstein
def rev(n):
	x = 0
	while n:
		x = x*10 + n%10
		n /= 10
	return x
n = int(raw_input('Enter a 3-digit number with the first and last digits differing by at least 2: '))
r = rev(n)
print 'Original: ', n
print 'Reverse: ', r
diff = n - r
diff = -diff if diff < 0 else diff
print 'Difference: ', diff
dr = rev(diff)
print 'Reverse: ', dr
print 'Sum: ', diff+dr

