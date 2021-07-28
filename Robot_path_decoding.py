def calc(listA):
    c = 1
    r = 1
    for i in listA:
        for j in i:
            if j == 'S':
                if r == 10**9:
                    r = 1
                else:
                    r += 1
            elif j == 'N':
                if r == 1:
                    r = 10**9
                else:
                    r -= 1
            elif j == 'W':
                if c == 1:
                    c = 10**9
                else:
                    c -= 1
            elif j == 'E':
                if c == 10**9:
                    c = 1
                else:
                    c += 1
    return c, r

T = int(input())
for f in range(T):
    inp = []
    listA = []
    while inp != 'y':
        ip = int(input())
        inn = input()
        inp = input()
        listA.append(inn*ip)
    print(f'case #{f+1}: {calc(listA)}')
