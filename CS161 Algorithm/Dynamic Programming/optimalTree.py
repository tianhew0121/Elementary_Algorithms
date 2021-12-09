from prettytable import PrettyTable

p = (0.21, 0.33, 0.1, 0.04, 0.02, 0.13, 0.17)


def draw_table(m):  # m is 2d array
    x = PrettyTable()
    for row in m:
        # x.add_row(row[1:])
        x.add_row(row)
    print(x)


def matrix(row, col, val):
    lst = list()
    for r in range(row+1):
        lst.append(list())
        for c in range(col+1):
            lst[r].append(val)
    return lst


def optimalTreeCost(p):
    n = len(p)
    E = matrix(n+1, n, 0)
    W = matrix(n+1, n, 0)
    root = matrix(n+1, n, 0)
    for i in range(1, n+2):
        for j in range(i, n+1):
            W[i][j] = W[i][j-1] + p[j-1]
    # draw_table(W[1:])
    for size in range(1, n+1):
        for i in range(1, n-size+2):
            j = i+size-1
            E[i][j] = float('inf')
            for r in range(i, j+1):
                #print('i,j:', i, j)
                #print('r:', r)
                x = E[i][r-1]
                x += E[r+1][j]
                x += W[i][j]
                # print(x)
                # draw_table(E)
                if x < E[i][j]:
                    E[i][j] = x
                    root[i][j] = r
                print('i,j:', i, j)
                print('r:', r)
                print('x:', x)
                draw_table(E)
                print()
    return E[1:], root[1:]


E, root = optimalTreeCost(p)
x = PrettyTable()
for row in E:
    # x.add_row(row[1:])
    x.add_row(row)
print(x)
x = PrettyTable()
for row in root:
    # x.add_row(row[1:])
    x.add_row(row)
print(x)
