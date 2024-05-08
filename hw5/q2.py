def merge_sorted_sequences(A, B):
    n = len(A)
    m = len(B)
    i = 0
    j = 0
    union = []

    while i < n and j < m:
        if A[i] < B[j]:
            union.append(A[i])
            i += 1
        elif A[i] > B[j]:
            union.append(B[j])
            j += 1
        else:
            union.append(A[i])
            i += 1
            j += 1

    while i < n:
        union.append(A[i])
        i += 1

    while j < m:
        union.append(B[j])
        j += 1

    return union

'''
Big O-Notation the most time complex runtime of this problem would be O(n+m)
n - the length of A and how many elements exist
m - the length of B and how many elements exist
'''