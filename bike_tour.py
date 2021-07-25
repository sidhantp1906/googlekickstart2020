def calc(listH):
    max = listH[0]
    for i in listH:
        if i >= max:
            max = i
        if listH[listH.index(max)-1] >= max or listH[listH.index(max)+1] >= max:
            max = 0

    return listH.count(max)

T = int(input())
for i in range(T):
    N = int(input())
    listH = []
    for j in range(N):
        H = int(input())
        listH.append(H)

    print(f'case #{i+1}: {calc(listH)}')
