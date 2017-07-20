from sys import stdin

test_num = 0
workers = []
for line in stdin:
    line = line.strip()
    line= line.split(' ')
    #print(line)
    if len(line) > 1 and len(line) <= 3:
        line = [int(x) for x in line]
        worker1 = line[0]
        worker2 = line[1]
        worker3 = line[2]
        #print(worker1)
        #print(worker2)
        #print(worker3)
        if worker1 > worker2 and worker1 < worker3:
            workers.append(worker1)

        elif worker1 < worker2 and worker1 > worker3:
            workers.append(worker1)

        elif worker2 > worker1 and worker2 < worker3:
            workers.append(worker2)

        elif worker2 < worker1 and worker2 > worker3:
            workers.append(worker2)
        else:
            workers.append(worker3)

for x in workers:
    test_num = test_num + 1
    print('Case ' + str(test_num)+':', (x))
