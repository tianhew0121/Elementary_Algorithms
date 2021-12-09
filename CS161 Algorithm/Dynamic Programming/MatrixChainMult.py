from prettytable import PrettyTable
#d = (40,2,100,50)
d = (6, 14, 19, 4, 15, 17, 10)


def matrix(row, col, val):
    lst = list()
    for r in range(row+1):
        lst.append(list())
        for c in range(col+1):
            lst[r].append(val)
    return lst


def optMatrixChain(d):
    n = len(d) - 1
    M = matrix(n, n, 0)
    S = matrix(n, n, 0)
    for length in range(2, n+1):
        for i in range(1, n-length+2):
            j = i+length-1
            M[i][j] = float('inf')
            for k in range(i, j):
                x = M[i][k] + M[k+1][j] + d[i-1] * d[k] * d[j]
                print('x:', x)
                print('k:', k)
                print('i, j:', i, j)

                if x < M[i][j]:
                    M[i][j] = x
                    S[i][j] = k
                x = PrettyTable()
                for row in M[1:]:
                    x.add_row(row[1:])
                    # x.add_row(row)
                print(x, '\n')
    return M[1:], S[1:]


M, S = optMatrixChain(d)
x = PrettyTable()
for m_row, s_row in zip(M, S):
    # x.add_row(row[1:])
    x.add_row(m_row)
    x.add_row(s_row)
print(x)
