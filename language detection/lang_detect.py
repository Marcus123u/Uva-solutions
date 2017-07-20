from sys import stdin


test_case = 0
lang_answers = []
english = 'ENGLISH'
spanish = 'SPANISH'
german = 'GERMAN'
french = 'FRENCH'
italian = 'ITALIAN'
russian = "RUSSIAN"
unknown = 'UNKNOWN'
for line in stdin:
    line = line.strip()
    if line == '#':
        for x in lang_answers:
            test_case = test_case + 1
            print('Case ' + str(test_case)+':', (x))
        exit()
    else:
        line = line.upper()
        #print(line)
        if line == 'HELLO':
            lang_answers.append(english)

        elif line == 'HOLA':
            lang_answers.append(spanish)

        elif line == 'HALLO':
            lang_answers.append(german)

        elif line == 'BONJOUR':
            lang_answers.append(french)

        elif line == 'CIAO':
            lang_answers.append(italian)

        elif line == 'ZDRAVSTVUJTE':
            lang_answers.append(russian)

        else:
            lang_answers.append(unknown)
