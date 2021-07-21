listK = []
listN = []
listP = []


def calc(listF, P):
    sum = 0

    for i in listF:
            for v in i:
                if P == 0:
                    return sum
                    break
                else:
                    sum += v
                    P = P-1

    #return sum


T = int(input())
for j in range(T):
    N = int(input())
    listN.append(N)
    P = int(input())
    listP.append(P)
    listF = []
    for f in range(N):
        K = int(input())
        listK.append(K)

        listA = []

        for i in range(K):
            A = int(input())
            listA.append(A)
        listF.append(listA)
        print(listA)
        print(listF)

    print(f'case #{j}: {calc(listF, P)}')
