from sys import stdin

quotes = 0
results = []
for line in stdin:
    line.strip()
    print(line)
    for item in line:
        if item == '"':
            # print(item)
            quotes = quotes + 1
            # print(quotes)
            if quotes % 2 == 1:
                results.append("``")
            else:
                results.append("''")
        else:
            results.append(item)
for x in results:
    print(x, end='')
