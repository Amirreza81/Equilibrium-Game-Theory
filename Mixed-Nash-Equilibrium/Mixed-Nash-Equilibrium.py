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
    N, M = list(map(int, input().split()))

    utility_1 = []
    utility_2 = []

    for i in range(N):
        utility_1.append([int(j) for j in input().split()])

    for i in range(N):
        utility_2.append([int(j) for j in input().split()])

    utility_1 = np.array(utility_1)
    utility_2 = np.array(utility_2)

    count = 0
    for i in range(2 ** N):
        if count != 0:
            break
        for j in range(2 ** M):
            if count != 0:
                break

            index1 = [k for k in range(N) if i & (1 << k)]
            A = []

            c = [0] * N + [0] * M
            c += [1, 1]

            index2 = [k for k in range(M) if j & (1 << k)]

            b = []

            if len(index2) == len(index1):
                list1 = [0] * (N + M + 2)
                for eee in range(N):
                    list1[eee] = 1

                new_list = []
                for x in list1:
                    new_list.append(-x)
                A.append(new_list)
                b.append(-1)

                A.append(list1)
                b.append(1)

                list1 = [0] * (N + M + 2)
                t = 0
                for www in range(N):
                    if www not in index1:
                        list1[t] = 1
                    else:
                        list1[t] = 0
                    t += 1

                A.append(list1)
                b.append(0)

                for k in range(N):
                    list1 = [0] * (2 + N + M)
                    list1[N + M] = -1
                    for q in range(M):
                        if q in index2:
                            list1[N + q] = utility_1[k][q]
                    if k in index1:
                        new_list = []
                        for x in list1:
                            new_list.append(-x)
                        A.append(new_list)
                        b.append(50)

                    A.append(list1)
                    b.append(-50)

                list1 = [0] * (N + M + 2)
                for aaaa in range(N, M + N):
                    list1[aaaa] = 1

                A.append(list1)
                b.append(1)

                new_list = []
                for x in list1:
                    new_list.append(-x)
                A.append(new_list)
                b.append(-1)

                list1 = [0] * (N + M + 2)
                t = 0
                for www in range(M):
                    if www not in index2:
                        list1[t + N] = 1
                    else:
                        list1[t + N] = 0
                    t += 1

                A.append(list1)
                b.append(0)

                for k in range(M):
                    list1 = [0] * (2 + N + M)
                    for q in range(N):
                        if q in index1:
                            list1[q] = utility_2[q][k]

                    list1[N + M + 1] = -1

                    if k in index2:
                        new_list = []
                        for x in list1:
                            new_list.append(-x)
                        A.append(new_list)
                        b.append(50)

                    A.append(list1)
                    b.append(-50)

                s = LPSolver(A, b, c)
                answer = s.solve()

                if answer[1] is not None:
                    for t in range(N):
                        print("{:.6f}".format(answer[1][t]), end=" ")
                    print()
                    for t in range(M):
                        print("{:.6f}".format(answer[1][N + t]), end=" ")
                    print()
                    count += 1

            else:
                continue


main()
