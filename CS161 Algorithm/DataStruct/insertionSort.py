# Work from left to right across array
# Insert each item in correct position with respect to (sorted)
# elements to its left
def insertionSort(n, A):
    for k in range(1, n):
        x = A[k]
        j = k - 1
        print("A[j]:", A[j], "A[k]:", A[k])
        while j >= 0 and A[j] > x:
            A[j+1] = A[j]
            j = j - 1

        A[j+1] = x
        print("array now is:", A)


lst = [43, 22, 55, 11, 91, 30]
lst1 = [43, 22, 55, 11, 91, 30]
insertionSort(len(lst), lst)
print("Sorting Complete:", lst)
print("control group:   ", sorted(lst1))


# Worst-case running time:
#       O(n^2)
