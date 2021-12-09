# Split array into two equal subarrays
# Sort both subarrays (recursively)
# Merge two sorted subarrays
from math import floor


def mergeSort(A, first, last):
    inv_count = 0
    if first < last:
        mid = floor((first + last) / 2)
        inv_count += mergeSort(A, first, mid)
        inv_count += mergeSort(A, mid+1, last)
        inv_count += merge(A, first, mid, mid+1, last)
    return inv_count


def merge(A, first1, last1, first2, last2):
    index1, index2, tempIndex, temp = first1, first2, 0, []
    inv_count = 0
    # Merge into temp array until one input array is exhausted
    while (index1 <= last1) and (index2 <= last2):
        if A[index1] <= A[index2]:
            temp.append(A[index1])
            tempIndex += 1
            index1 += 1
        else:
            temp.append(A[index2])
            tempIndex += 1
            index2 += 1
            ###########count inversion ###########
            print('2 elements are:', A[index1], A[index2-1])
            inv_count += last1 - index1 + 1
            print('Inv count:     ', inv_count)
            ###########count inversion ###########
    # copy trailer portion
    while index1 <= last1:
        temp.append(A[index1])
        tempIndex += 1
        index1 += 1

    while index2 <= last2:
        temp.append(A[index2])
        tempIndex += 1
        index2 += 1
    # copy temp array back to A
    index = first1
    tempIndex = 0
    while index <= last2:

        A[index] = temp[tempIndex]
        index += 1
        tempIndex += 1
    return inv_count


lst = [21, 25, 32, 87, 27, 96, 75, 31]
lst1 = [21, 25, 32, 87, 27, 96, 75, 31]
inv_count = mergeSort(lst, 0, len(lst)-1)
print('Control:    ', sorted(lst1))
print('Merge Sort: ', lst)
print('Inversions: ', inv_count)
