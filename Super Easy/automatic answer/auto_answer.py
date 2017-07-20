from sys import stdin


runs = stdin.readline()
runs = int(runs)
while runs != 0:
    line = stdin.readline()
    line = line.strip()
    line = line.split(' ')
    # print(line)
    # if len(line) < 2:
    #     if runs == 1:
    #         break
            #print("if statment ran")
    line = [int(x) for x in line]
    start = line[0]
    step1 = start * 567 / 9 + 7492
    step2 = step1 * 235 / 47 - 498
    #print(step2)
    step2 = int(step2)
    step2 = str(step2)
    print(step2[-2])
    runs=runs-1
