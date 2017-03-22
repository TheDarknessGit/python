f = open('example.txt', 'r')
#print f.readline();
#print f.readline();
#print f.readline();
x = 1
for line in f:
    if line != "\n":
        print str(x) + " ~ " + line
        x += 1
