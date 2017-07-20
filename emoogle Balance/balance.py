from sys import stdin

not_zero = 0
zero = 0
for line in stdin:
    line = line.strip()
    line = line.split(' ')
    line = [int(x) for x in line]
    if line == "0":
        exit()
        print("if")
    else:
        ("else")
        for item in line:
            if item == "0":
                zero = zero + 1
                print("its a zero")
            else:
                not_zero = not_zero + 1
                print("it's not a zero")
        #print(not_zero-zero)
