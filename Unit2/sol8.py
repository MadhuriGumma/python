# prob8: Tones
# weird that loops have been forbidden
from math import pow
def findFreq(pair):
	octave = int(pair)
	pitch = int(pair*10) % 10
	print 'Octave: ', octave
	print 'Pitch class: ', pitch
	o = octave - 4.0
	m = pitch - 9.0
	return 440*pow(2, o + m/12.0)

print 'Printing octpch values!'
pair = float(raw_input('enter octpch pair: '))
print 'Frequency: ', findFreq(pair), ' Hz'

