from sys import stdin
zero = 0
numbers = False
answer = []
for line in stdin:
    line = line.strip()
    line = line.split(' ')
    #print(line)
    line = [int(x) for x in line]
    if len(line) > 1:
            #print(line)
            high = max(line)
            low = min(line)
            #print(high)
            #print(low)
            answer.append((high - low) * 2)
    else:
        for item in line:
            if item == 1:
                answer.append(zero)
                for i in range(len(answer) - 1):
                    if answer[i] == 0 and answer[i+1] == 0:
                        answer.remove(i)

for x in answer:
     print(x)
