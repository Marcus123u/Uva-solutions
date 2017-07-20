from sys import stdin

def main():
    case = 0
    while True:
        case += 1
        zero = 0
        not_zero = 0
        query = stdin.readline()
        query = query.strip()
        query = int(query)
        if query == 0:
            exit()
        else:
            line = stdin.readline()
            line = line.strip()
            line = line.split(' ')
            line = [int(x) for x in line]
            for num in line:
                if num > 0:
                    zero = zero + 1
                else:
                    not_zero = not_zero + 1

            print("Case " + str(case) + ": " + str(zero - not_zero))

if __name__ == '__main__':
    main()
