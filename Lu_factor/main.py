import numpy as np


def lu(matrix, b, n):
    n2 = n
    y = np.zeros((n2, 1))
    x = np.zeros((n2, 1))
    Ufactor = matrix.copy()
    Lfactor = np.identity(len(matrix))
    for n in range(0, len(matrix) - 1):
        for m in range(n + 1, len(matrix)):
            Lfactor[m, n] = Ufactor[m, n] / Ufactor[n, n]
            Ufactor[m, :] += -Lfactor[m, n] * Ufactor[n, :]
    for i in range(n):
        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += Lfactor[i][j] * Ufactor[j][k]
            Ufactor[i][k] = matrix[i][k] - sum

    y[0][0] = b[0][0]
    for i in range(1, n2):
        sum = b[i][0]
        for j in range(n2):
            if (i != j):
                sum = sum - (Lfactor[i][j] * y[j])
            else:
                break

        y[i][0] = sum
    x[n2 - 1][0] = y[n2 - 1][0] /Ufactor[n2-1][n2 - 1]
    for i in range(n2 - 2, -1, -1):
        sum = y[i][0]
        for j in range(n2 - 1,-1, -1):
            if (i != j):
                sum = sum - (Ufactor[i][j] * x[j])
            else:
                break
        x[i][0] = sum / Ufactor[i][j]

    for i in range(n2):
        print(x[i][0], end=" ")
    print("")

init = input()
init=init.split()
n = int(init[0])
m = int(init[1])
matrix = np.zeros((n, n))
for i in range(n):
    x = input()
    x2 = x.split()
    for j in range(n):
        matrix[i][j] = int(x2[j])

b = np.zeros((n, 1))

for i in range(m):
    x = input()
    x2 = x.split()
    for j in range(n):
        b[j][0] = int(x2[j])
    lu(matrix, b, n)
