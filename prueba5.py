__author__ = 'Karl Fischer'


for x in range(1,100,1):
    a = False
    b = False
    if x % 3 == 0:
        a = True
    if x % 5 == 0:
        b = True

    if a and b:
        print "ZigZag"
    elif a:
        print "Zig"
    elif b:
        print "Zag"
    else:
        print x