# Split problem into subproblem(s)
# Solve each subproblem (usually via recursive call)
# Combine solution of subproblem(s) into solution of original
# problem


def quickSort(A, first, last):
    if first < last:
        split_point = split(A, first, last)
        print('Pivot:  ', A[split_point])
        print('Split:  ', A[first:split_point],
              '   -   ',  A[split_point+1:last+1])
        quickSort(A, first, split_point - 1)

        quickSort(A, split_point + 1, last)


def split(A, first, last):
    split_point = first
    x = A[first]
    for k in range(first+1, last+1):
        if A[k] < x:
            temp = A[split_point+1]
            A[split_point+1] = A[k]
            A[k] = temp
            split_point += 1
    temp = A[first]
    A[first] = A[split_point]
    A[split_point] = temp

    return split_point


lst = [27, 83, 23, 36, 15, 79, 22, 18]
lst1 = [27, 83, 23, 36, 15, 79, 22, 18]
quickSort(lst, 0, len(lst) - 1)
print('Quick Sort:      ', lst)
print('Control group:   ', sorted(lst1))


# Facts about quick sort:
# Suppose S is the sorted lst
# the chance for si and sj to be compared is 2 / (j-i + 1) for i < j
