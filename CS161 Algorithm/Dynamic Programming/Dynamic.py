# This file has an implementation of dynamic programing version of Truck Loading (subset-sum) problem.
# Problem definition:
# Truck has weight limit of W .
#   n boxes. Box i has weight wi.
#   We want to load the truck to carry the maximum weight
#   possible, subject to the weight restriction.

W = 100
w = [0, 90, 90]
OPT = None  # 2d matrix, n x W    n number of box, W weight limit of truck
n = len(w)-1


def matrix(row, col, val):
    lst = list()
    for r in range(row+1):
        lst.append(list())
        for c in range(col+1):
            lst[r].append(val)
    return lst


def dynamic_load_truck(W, w, n):
    OPT = matrix(n, W, 0)
    keep = matrix(n, W, 0)
    for i in range(1, n+1):
        for j in range(1, W+1):
            if w[i] > j or (w[i] + OPT[i-1][j-w[i]] <= OPT[i-1][j]):
                OPT[i][j] = OPT[i-1][j]
                keep[i][j] = False
            else:
                OPT[i][j] = w[i] + OPT[i-1][j-w[i]]
                keep[i][j] = True
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


OPT, keep = dynamic_load_truck(W, w, n)
output_result(OPT, keep, n, W)
