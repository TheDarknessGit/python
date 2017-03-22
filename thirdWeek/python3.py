f = open('example2.txt', 'a')
x = range(1,10)
for line in x:
    f.write("This is line number " + str(line) + "\n")
f.close()
