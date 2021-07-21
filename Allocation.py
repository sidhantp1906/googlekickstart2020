listB = []
listN = []

def calc(B, listA):
    listA.sort()
    c = 0
    for ch in listA:
        if ch <= B:
            B -= ch
            c += 1
    return c

T = int(input())
for k in range(T):
    B = int(input())
    listB.append(B)
    N = int(input())
    listN.append(N)
    listA = []

    for i in range(N):
        A = int(input())
        listA.append(A)
    print(f'case #{k}: {calc(B, listA)}')
