# Problem24: GDP and Unemployability

def getgdpavg(filename, year):	
	with open(filename) as g:
		glist = g.read().strip().split(",")
	s = 0.0
	si = (year - 1948)*4
	for i in range(si, si + 4):
		s = s + float(glist[i])
	return s/4.0

def getunempavg(filename, year):
	with open(uf) as u:
		ulist = u.read().strip().split(",")
		si = (y - 1948)*12
		s = 0.0
	for i in range(si, si + 12):
		s = s + float(ulist[i])
	return s/12.0

gf = raw_input("Enter GDP filename: ")
uf = raw_input("Enter Unemployment filename: ")
y = int(raw_input("Year to examine: "))
while y < 1948 or y > 2008:
	print "Bad year, try again"
	y = int(raw_input("Year to examine: "))

g = getgdpavg(gf, y)
u = getunempavg(uf, y)
print "GDP:", g
print "Unemployment:", u

