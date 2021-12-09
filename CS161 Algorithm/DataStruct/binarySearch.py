# Input is a sorted array A and an item x.
# Problem is to locate x in the array.
from math import floor, log


def binarySearch(A, x, first, last):
    if first > last:
        return -1
    else:
        mid = floor((first+last)/2)
        if x == A[mid]:
            return mid
        elif x < A[mid]:
            return binarySearch(A, x, first, mid-1)
        else:
            return binarySearch(A, x, mid+1, last)


# binarySearch(A, x, 0, n-1) n is len(A)
#           1   if n = 1
# T(n) =
#           1 + T(floor(n/2))   otherwise
# Solution: T(n) = floor(lg(n)) + 1
#       Therefore Binary Search does floor(lg(n)) + 1 3-way comparisons
#       on array of size n in the worst case.
n = 1024
print("Worst case 3-way comparison of binary search is :", log(n, 10) + 1)
