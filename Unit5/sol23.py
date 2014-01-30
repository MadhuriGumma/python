# Problem 23: WeFeelFine
# API broken
import urllib
u = raw_input("Enter URL: ")
conn = urllib.urlopen(u)
data = conn.read()
conn.close()
print data
