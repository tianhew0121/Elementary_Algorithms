from random import choice


class KOutOfRangeException(Exception):
    pass


def QuickSelect(S, k):
    if k > len(S):
        raise KOutOfRangeException()
    if len(S) == 1:
        return S[0]
    m_ = choice(S)
    #m_ = 43
    L = [i for i in S if i < m_]
    E = [i for i in S if i == m_]
    G = [i for i in S if i > m_]
    print(L, E, G)
    if len(L) >= k:
        return QuickSelect(L, k)
    elif len(L) + len(E) >= k:
        return m_
    else:
        return QuickSelect(G, k - (len(L) + len(E)))


lst = [66, 42, 85, 80, 11, 87, 40, 47, 15, 43, 76, 32]
print(QuickSelect(lst, 6))
