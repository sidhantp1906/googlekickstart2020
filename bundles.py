lists = []


def calc(listB):
    c = 0
    for j in range(len(listB)-1):
        for i in listB[j]:
            for k in listB[j + 1]:
                if i == k:
                    c += 1

        return c


T = int(input())
for f in range(T):
    inp = int(input())
    k = int(input())
    for l in range(inp):
        s = input()
        lists.append(s)
    for i in range(len(lists)//k):
        listB = []
        for j in range(k):
            a = int(input())
            b = lists[a]
            listB.append(b)
        #print(listB)

    #print(lists)
    print(f'case #{f+1}: {calc(listB)}')
