f_name = 'com_rev.dat'
fh = open(f_name)
count = 0
for line in fh:
    line = line.rstrip()
    if not count:
        print(line)
    else:
        print(count, line)
    count += 1