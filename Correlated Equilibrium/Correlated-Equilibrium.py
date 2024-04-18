import math

import numpy as np
from math import inf


class LPSolver(object):
    EPS = 1e-9
    NEG_INF = -inf

    def __init__(self, A, b, c):
        self.m = len(b)
        self.n = len(c)
        self.N = [0] * (self.n + 1)
        self.B = [0] * self.m
        self.D = [[0 for i in range(self.n + 2)] for j in range(self.m + 2)]
        self.D = np.array(self.D, dtype=np.float64)
        for i in range(self.m):
            for j in range(self.n):
                self.D[i][j] = A[i][j]
        for i in range(self.m):
            self.B[i] = self.n + i
            self.D[i][self.n] = -1
            self.D[i][self.n + 1] = b[i]
        for j in range(self.n):
            self.N[j] = j
            self.D[self.m][j] = -c[j]
        self.N[self.n] = -1
        self.D[self.m + 1][self.n] = 1

    def pivot(self, r, s):
        D = self.D
        B = self.B
        N = self.N
        inv = 1.0 / D[r][s]
        dec_mat = np.matmul(D[:, s:s + 1], D[r:r + 1, :]) * inv
        dec_mat[r, :] = 0
        dec_mat[:, s] = 0
        self.D -= dec_mat
        self.D[r, :s] *= inv
        self.D[r, s + 1:] *= inv
        self.D[:r, s] *= -inv
        self.D[r + 1:, s] *= -inv
        self.D[r][s] = inv
        B[r], N[s] = N[s], B[r]

    def simplex(self, phase):
        m = self.m
        n = self.n
        D = self.D
        B = self.B
        N = self.N
        x = m + 1 if phase == 1 else m
        while True:
            s = -1
            for j in range(n + 1):
                if phase == 2 and N[j] == -1:
                    continue
                if s == -1 or D[x][j] < D[x][s] or D[x][j] == D[x][s] and N[j] < N[s]:
                    s = j
            if D[x][s] > -self.EPS:
                return True
            r = -1
            for i in range(m):
                if D[i][s] < self.EPS:
                    continue
                if r == -1 or D[i][n + 1] / D[i][s] < D[r][n + 1] / D[r][s] or (D[i][n + 1] / D[i][s]) == (
                        D[r][n + 1] / D[r][s]) and B[i] < B[r]:
                    r = i
            if r == -1:
                return False
            self.pivot(r, s)

    def solve(self):
        m = self.m
        n = self.n
        D = self.D
        B = self.B
        N = self.N
        r = 0
        for i in range(1, m):
            if D[i][n + 1] < D[r][n + 1]:
                r = i
        if D[r][n + 1] < -self.EPS:
            self.pivot(r, n)
            if not self.simplex(1) or D[m + 1][n + 1] < -self.EPS:
                return self.NEG_INF, None
            for i in range(m):
                if B[i] == -1:
                    s = -1
                    for j in range(n + 1):
                        if s == -1 or D[i][j] < D[i][s] or D[i][j] == D[i][s] and N[j] < N[s]:
                            s = j
                    self.pivot(i, s)
        if not self.simplex(2):
            return self.NEG_INF, None
        x = [0] * self.n
        for i in range(m):
            if B[i] < n:
                x[B[i]] = round(D[i][n + 1], 6)
        return round(D[m][n + 1], 6), x


def main():
    N, M = list(map(float, input().split()))
    X, Y = list(map(int, input().split()))
    utilities_1 = []
    utilities_2 = []
    for i in range(X):
        row = list(map(float, input().split()))
        for j in range(2 * Y):
            if j % 2 == 0:
                utilities_1.append(row[j])
            else:
                utilities_2.append(row[j])

    A = []
    b = []

    # Same constraint for all inputs => p1 + p2 + p3 + p4 = 1
    sum_list = []
    for i in range(X * Y):
        sum_list.append(1.0)
    A.append(sum_list)
    b.append(1.0)

    sum_list = []
    for i in range(X * Y):
        sum_list.append(-1.0)
    A.append(sum_list)
    b.append(-1.0)

    # player 1:
    k = -1
    if X != 1:
        for i in range(math.ceil(X)):
            k += 1
            q = -1
            for h in range(X):
                list_of_utilities = [0 for i in range(X * Y)]
                q += 1
                for j in range(Y):
                    list_of_utilities[(j + k * Y)] = utilities_1[(j + (k + q + 1) * Y) % (X * Y)] - \
                                                     utilities_1[(j + k * Y)]
                A.append(list_of_utilities)
                b.append(0.0)

    # player 2:
    k = -1
    if X != 1:
        for i in range(math.ceil(Y)):
            k += 1
            q = -1
            for h in range(Y):
                list_of_utilities = [0 for i in range(X * Y)]
                q += 1
                for j in range(X):
                    list_of_utilities[(k + j * Y)] = utilities_2[((k + 1 + q) % Y + j * Y) % (X * Y)] - \
                                                     utilities_2[(k + j * Y)]
                A.append(list_of_utilities)
                b.append(0.0)

    c = [0 for i in range(X * Y)]
    for i in range(X * Y):
        c[i] = N * utilities_1[i] + M * utilities_2[i]

    s = LPSolver(A, b, c)
    answer = s.solve()

    print("{:.6f}".format(answer[0]))
    for i in range(X * Y):
        print("{:.6f}".format(answer[1][i]), end=" ")
        if i % Y == Y - 1:
            print()


if __name__ == '__main__':
    main()
