# O(n), O(n + max(A))
def counting_sort(A):
    B = [0 for _ in range(len(A))]
    C = [0 for _ in range(max(A)+1)]

    for i in range(len(A)):
        C[A[i]] = C[A[i]]+1

    for j in range(1, len(C)):
        C[j] += C[j-1]

    for k in range(len(A)-1, -1, -1):
        B[C[A[k]]-1] = A[k]
        C[A[k]] -= 1

    return B

A = [2,5,3,1,2,3,1,3]
print(counting_sort(A))
