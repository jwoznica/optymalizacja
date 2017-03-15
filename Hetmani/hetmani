# Problem: Hetmani dla dowolnego n
n = 5
print 'Maximize'
print 'obj:',
for x in range(ord('a'), ord('a') + n):
    for y in range(1, n + 1):
        print '+',
        print chr(x) + str(y),
print ''
print ''
print 'Subject To'
print 'cap:'
for x in range(2,n+2):
    for y in range(1,x):
        print '+ ' + chr(ord('a')+x-y-1) + str(y),
    print ' <= 1'
for x in range(1,n):
    for y in range(x+1,n+1):
        print '+ ' + chr(ord('a')+x-y+n) + str(y),
    print ' <= 1'
for x in range(1,n+1):
    for y in range(1,x+1):
        print '+ ' + chr(ord('a')+n-x+y-1) + str(y),
    print ' <= 1'
for x in range(n+1,2*n):
    for y in range(x,2*n):
        print '+ ' + chr(ord('a')-x+y) + str(y-n+1),
    print ' <= 1'
print ''
print 'Bounds'
for x in range(ord('a'), ord('a') + n):
    for y in range(1, n + 1): 
        print '0 <= ' + chr(x) + str(y) + ' <= 1'
print ''
print 'Generals'
for x in range(ord('a'), ord('a') + n):
    for y in range(1, n + 1): 
        print chr(x) + str(y)
print ''
print 'End'
