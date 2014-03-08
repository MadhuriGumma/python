# Problem 27 - Rating Players
keys = []
p = []
def readplayers(ff):
	global keys, p
	with open(ff) as f:
		d = f.read().strip()
	p = []
	ls = d.split("\n")
	keys = ls[0].split(",")
	for i, l in enumerate(ls[1:]):
		pl = l.split(",")
		for m in range(6, len(pl)):
			if pl[m] == 'NULL' or pl[m] == 'N':
				pl[m] = 0
			else:
				pl[m] = int(pl[m].strip())
		p.append(pl)

def eff(pl):
	if pl[6]:
		a = ((pl[8])+(pl[11])+(pl[12])+(pl[13])+(pl[14]))
		b = (((pl[17]) - (pl[18])) + ((pl[19]) - (pl[20])) + (pl[15]))
		return (a - b)/pl[6]
	else:
		return 0

if __name__ == '__main__':
	readplayers('player_regular_season.csv')
	effs = []
	for pl in p:
		effs.append([eff(pl), pl[2]+" "+pl[3]])
	effs.sort()
	effs.reverse()
	with open('top50', 'w') as f:
		for e in effs[:50]:
			f.write(e[1] + ":" + str(e[0])+"\n")
	
	
