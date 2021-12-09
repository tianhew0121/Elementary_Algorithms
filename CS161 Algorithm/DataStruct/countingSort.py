def countingSort(A, B, n, k):
    locator = [0]*(k+1)
    for i in range(1, n+1):
        locator[A[i]] = locator[A[i]] + 1

    for x in range(2, k+1):
        locator[x] = locator[x] + locator[x-1]
    print('locator is:', locator)
    for i in reversed(range(1, n+1)):
        print('elemnt copied: ', A[i])
        print('Stored at    : ', locator[A[i]])
        B[locator[A[i]]] = A[i]
        locator[A[i]] = locator[A[i]] - 1
# O(n + k)


A = [0, 3, 4, 1, 3, 2, 1, 1, 4, 3]
k = max(A)
B = [0] * len(A)
countingSort(A, B, len(A)-1, k)
print(B[1:])
