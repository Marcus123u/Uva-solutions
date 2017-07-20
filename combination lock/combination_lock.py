from sys import stdin

def main():

    for line in stdin:
        line = line.strip()
        if line == "0 0 0 0":
            exit()

        else:
            line = line.split(' ')
            line = [int(x) for x in line]
            total_degrees = 0
            start = line[0]
            first = line[1]
            second = line[2]
            third = line[3]
            total_degrees += 720
            total_degrees += (start - first + 40) % 40 * 9
            total_degrees += 360 +(second - first + 40) % 40 * 9
            total_degrees += (second - third + 40) % 40 * 9
            print(total_degrees)
if __name__ == '__main__':
    main()
