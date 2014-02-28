# Problem24: GDP and Unemployability
import numpy as np
import matplotlib.pyplot as pl

glist = {}
ulist = {}

def readgdp(gf):
	global glist
	with open(gf) as g:
		r = g.read().strip().split("\n")
		for i in range(1948, 2010):
			arr = [float((x.split(" "))[-1]) for x in r if x[:4] == str(i)]
			if arr:
				glist[i] = sum(arr)/len(arr)

def readunemp(uf):
	global ulist
	with open(uf) as u:
		r = u.read().strip().split("\n")[1:]
		for i in range(0, len(r)):
			arr = r[i].replace(",", " ").strip().split(" ")
			vals = map(float, arr[1:])
			y = int(arr[0])
			if vals:
				avg = sum(vals)/len(vals)
				ulist[y] = avg

def fetchyear(y):
	if y not in glist or y not in ulist:
		print "Year out of range! Try again..."
		return 0
	else:
		print "Average GDP in", y, ":", glist[y]
		print "Average unemployment in", y, ":", ulist[y]
		return 1
def showgraph():
	global ulist, glist
	fig = pl.figure()
	ax1 = fig.add_subplot(111)
	xr = np.arange(1948, 2008, 1)
	y1 = [(glist[i+1]-glist[i])*100/glist[i] for i in range(1948, 2008)]
	ax1.plot(xr, y1, 'b-')
	ax1.set_xlabel('Year')
	ax1.set_ylabel('Change in GDP')
	
	ax2 = ax1.twinx()
	y2 = [ulist[x] for x in range(1948, 2008, 1)]
	ax2.plot(xr, y2, 'r-')
	ax2.set_ylabel('Unemployment rate')
	ax1.set_title('Change in GDP vs Unemployment')
	pl.show()
	
if __name__ == "__main__":
	readgdp("gdp.txt")
	readunemp("unemp.csv")
	while not fetchyear(int(raw_input("Enter year: "))):
		pass
	if raw_input("Enter Y to generate graph: ").lower() == 'y':
		showgraph()

