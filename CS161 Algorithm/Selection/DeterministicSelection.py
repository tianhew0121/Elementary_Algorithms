from math import ceil, floor


def bruteForceSelect(S, k):
    return sorted(S)[k]


def divide(l):
    if len(l) >= 5:
        return l[:5]
    else:
        return l


def getGroupOfFive(lst):
    result = []
    for i in range(int(len(lst)/5)):
        result.append(divide(lst))
        lst = lst[5:]
    result.append(divide(lst))
    return result


def DSelect(S, k):
    n = len(S)
    group = None
    group_median = []
    if n <= 5:
        return bruteForceSelect(S, k)
    # // step 1: divide into group of 5
    group = getGroupOfFive(S)
    # // step 2: compute median of each group of 5
    for i in range(len(group)):
        group_median.append(bruteForceSelect(
            group[i], floor(len(group[i])/2)))
    # // step 3: compute m_ = median of group medians
    print('groups are :', group)
    m_ = DSelect(group_median, ceil(len(group)/2))
    # // step 4: partition elements of S in L E G
    L = [i for i in S if i < m_]
    E = [i for i in S if i == m_]
    G = [i for i in S if i > m_]
    # // step 5: return m_ or recursively call DSelect in L or G
    print('L:', L)
    print('E:', E)
    print('G:', G)
    print('k:', k)
    if len(L) >= k:
        return DSelect(L, k)
    elif len(L) + len(E) >= k:
        return m_
    else:
        return DSelect(G, k - (len(L) + len(E)) - 1)


lst1 = [37, 73, 31, 18, 23, 54, 90, 20, 34, 70, 98, 15,
        25, 19, 66, 24, 84, 49, 92, 83, 93, 35, 71, 39, 44]
print(DSelect(lst1, 10))
