from math import floor


def FindMax(H):
    return H[0]  # find max of heap


def ExtractMax(H):
    x = H[0]
    Delete(H, 0)
    return x
    # find maxi and delete it from heap


def insert(H, x):
    H = H.append(0)
    k = len(H) - 1
    H[k] = x
    siftUP(H, k)
    # insert x into H


def Delete(H, i):
    k = len(H) - 1
    H[i] = H[k]
    H.pop(-1)
    siftUP(H, i)
    siftDOWN(H, i)
    # delete item at location i from heap


def siftUP(H, i):
    parent = (i-1) / 2
    if i > 0 and H[parent] < H[i]:
        temp = H[i]
        H[i] = H[parent]
        H[parent] = temp
        siftUP(H, parent)
# Move the item at location i up to its correct
# position by repeatedly swapping the item with its parent, as
# necessary


def siftDOWN(H, i):
    n = len(H)  # number of itme in heap
    left = 2 * i + 1
    right = 2 * i + 2
    if right < n and H[right] > H[left]:
        largerChild = right
    else:
        largerChild = left
    if largerChild < n and H[i] < H[largerChild]:
        temp = H[i]
        H[i] = H[largerChild]
        H[largerChild] = temp
        siftDOWN(H, largerChild)
# Move the item at location i down to its
# correct position by repeatedly swapping the item with the child
# having the larger key, as necessary.


def heapify(H, n):
    for i in reversed(range(0, n)):
        siftDOWN(H, i)


def heapSort(A, n):
    heapify(A, n)
    for k in reversed(range(0, n)):
        A[k] = ExtractMax(A)


heap2 = [98, 81, 66, 73, 41, 19, 50, 67, 42, 32, 20, 15]
ExtractMax(heap2)
print(heap2)
