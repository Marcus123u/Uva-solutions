from sys import stdin

def main():

    for line in stdin:
        line = line.strip()
        if line == '0 0':
            exit()
        else:
            line = line.split(' ')
            #print(line)
            length = len(line)
            print(length)
            if length > 1:
                line = [int(x) for x in line]

                first = line[0]
                second = line[1]
                print((first // 3) * (second // 3))
            else:
                exit()

if __name__ == '__main__':
    main()
