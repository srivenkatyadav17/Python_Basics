f = open('C://Users//srive//PycharmProjects//funny.txt', 'r')
f_out = open('C://Users//srive//PycharmProjects//funny_wc.txt', 'w')
for line in f:
    tokens = line.split(' ')
    f_out.write('Word count:' + str(len(tokens)) + line)
f.close()
f_out.close()
