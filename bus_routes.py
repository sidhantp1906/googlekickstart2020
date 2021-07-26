def calc(day, listX):
    lista = []
    for i in range(len(listX)):
        if (day - listX[i]) // listX[i] == 0:
            return listX[i]
            lista.append(listX[i])
        elif day % listX[i] == 0:
            lista.append(day)
            return day
        else:
            X = day - listX[i]
            Z = X // listX[i]
            Y = Z * listX[i]
            lista.append(Y)
            return Y
    return lista[0]





T = int(input('tc : '))
for i in range(T):
    N = int(input('n: '))
    Day = int(input('D: '))
    listX = []
    for j in range(N):
        X = int(input('X: '))
        listX.append(X)
    print(f'case #{i+1}: {calc(Day, listX)}')
