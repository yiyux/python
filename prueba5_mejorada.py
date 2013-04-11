__author__ = 'kfischer'


for x in range(1,100,1):
    print "",
    if x % 3 == 0:
        print "Zig",
    if x % 5 == 0:
        print "Zag"
    if not(x % 3 == 0) and not(x % 5 == 0):
        print x
