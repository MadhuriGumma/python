# prob4: Population
init = 307357870
s = raw_input('enter number of years')
years = int(s)
time = years*365*24*3600
res = init + time/7 - time/13 + time/35
print 'Population: ', res
