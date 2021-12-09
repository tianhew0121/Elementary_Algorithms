# 0/1 knapsack problem
from prettytable import PrettyTable


W = 15
v = [0, 6, 10, 11, 9, 3, 11]
w = [0, 7, 5, 9, 3, 2, 6]
OPT = None  # 2d matrix, n x W    n number of box, W weight limit of truck
n = len(w)-1


def matrix(row, col, val):
    lst = list()
    for r in range(row+1):
        lst.append(list())
        for c in range(col+1):
            lst[r].append(val)
    return lst


def dynamic_knapsack(W, w, v, n):
    OPT = matrix(n, W, 0)
    keep = matrix(n, W, 0)
    for i in range(1, n+1):
        for j in range(1, W+1):
            if w[i] > j or (v[i] + OPT[i-1][j-w[i]] <= OPT[i-1][j]):
                print('OPT[i-1][j]:', OPT[i-1][j])
                print('i,j:', i, j)
                print('w[i]:', w[i])
                print('v[i] + OPT[i-1][j-w[i]]:', v[i] + OPT[i-1][j-w[i]])
                OPT[i][j] = OPT[i-1][j]
                keep[i][j] = False
                x = PrettyTable()
                for row, k in zip(OPT, keep):
                    # x.add_row(row[1:])
                    x.add_row(row)
                    x.add_row(k)
                print(x)
            else:
                print('OPT[i-1][j]:', OPT[i-1][j])
                print('i,j:', i, j)
                print('w[i]:', w[i])
                print('v[i] + OPT[i-1][j-w[i]]:', v[i] + OPT[i-1][j-w[i]])
                OPT[i][j] = v[i] + OPT[i-1][j-w[i]]
                keep[i][j] = True
                x = PrettyTable()
                for row, k in zip(OPT, keep):
                    # x.add_row(row[1:])
                    x.add_row(row)
                    x.add_row(k)
                print(x)
    return OPT, keep


def output_result(OPT, keep, i, j):
    #i, j = i+1, j+1
    if i == 0:
        return
    if keep[i][j]:
        output_result(OPT, keep, i-1, j-w[i])
        print(w[i])
    else:
        output_result(OPT, keep, i-1, j)


OPT, keep = dynamic_knapsack(W, w, v, n)
output_result(OPT, keep, n, W)
x = PrettyTable()
for row, k in zip(OPT, keep):
    # x.add_row(row[1:])
    x.add_row(row)
    x.add_row(k)
print(x)
