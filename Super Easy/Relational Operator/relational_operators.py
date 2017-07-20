from sys import stdin

for line in stdin:
    line = line.strip()
    line = line.split(' ')
    #print(line)
    if len(line) >= 2:
        line = [int(x) for x in line]
        first = line[0]
        second = line[1]
        if first > second:
            print(">")
        elif first < second:
            print("<")
        else:
            print("=")
