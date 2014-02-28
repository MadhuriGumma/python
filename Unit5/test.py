import random as r
l = (2008 - 1948 + 1)*12
s = ""
for i in range(l):
	s = s + str(r.randint(300, 500)/100.0)
	if i < l-1:
		s = s + ","
print s
