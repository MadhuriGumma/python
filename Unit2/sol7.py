# prob7: MacArthur
month = int(raw_input('enter your birth month[1 for Jan, 2 for Feb and so on]: '))
age = int(raw_input('enter your age: '))
x = (2*month + 5)*50 + age - 365
print 'Special number: ', x
x += 115
na = x % 100
x /= 100
nm = x%10
print 'Age: ', na
print 'Month: ', nm

