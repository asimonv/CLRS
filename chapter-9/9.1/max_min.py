
# O(3*floor(n/2)), O(1) space
# Compare by elements by pairs:
#   1. check which is min, max
#   2. check if min is < min
#   3. check if max is > max
# floor(n/2) iterations, 3 comparisons
# by pair.
def max_min(A):
    max, min = A[0], A[0]
    for i in range(0, len(A), 2):
        if A[i] < A[i+1]:
            if A[i] < min:
                min = A[i]
            if A[i+1] > max:
                max = A[i+1]
        else:
            if A[i] > max:
                max = A[i]
            if A[i+1] < min:
                min = A[i+1]

    return max, min

A = [1,9,3,4,6,-2,8,43,12,10]
print(max_min(A))
