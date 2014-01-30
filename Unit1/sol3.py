s = raw_input('enter float value: ')
m = float(s)
print m
bcd = m*1610*117.647*24
ff = m*1760*24*14/220
mach = m*3*1760/1130/3600
psl = (m*1610/36)/299792458
print bcd
print ff
print mach
print psl
"""
x*3600/1609.34
1mach = 1130ft/sec
1 mile = 1760 yards
1meter = 117.647 bc
1mile = 1609.34meters
"""
