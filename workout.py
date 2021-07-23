listN = []
listK = []
lists = []

def calc(listM):
    for m in range(len(listM)-1):
        diff = listM[m+1] - listM[m]
        lists.append(diff)
    lists.sort()
    max = lists[0]
    for i in lists:
        if i >= max:
            max = i

    return max

T = int(input('tc: '))
for i in range(T):
    N = int(input('ses: '))
    listN.append(N)
    K = int(input('add: '))
    listK.append(K)

    listM = []
    for j in range(N):
        M = int(input('hr: '))
        listM.append(M)
    for k in range(K):
        A = int(input('addt: '))
        ind = int(input('ind: '))
        listM.insert(ind, A)
    print(listM)
    print(f'case #{i+1}: {calc(listM)}')
