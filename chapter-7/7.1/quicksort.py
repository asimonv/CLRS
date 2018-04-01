# O(n), O(1) space
# 1. Select pivot (last element),
# 2. Set wall to be at left most
# position of the sublist.
# 3. Iterate. If curr element is
# smaller than the pivot, swap it
# with the left most element after
# the wall (A[wall]), then move the
# wall one position to the right.
# 4. By this point, every element
# that is smaller or equal than the
# pivot, is going to be at the left
# of the wall, so swap the pivot with
# the first element after the wall so
# the pivot goes into it's place in the
# sublist.
def partition(A, p, q):
    x = A[q]
    wall = p
    for i in range(p, q):
        if A[i] <= x:
            A[wall], A[i] = A[i], A[wall]
            wall += 1
    A[q], A[wall] = A[wall], A[q]

    return wall

# O(nlgn), O(1) space
# After the partition was done
# the pivot will be at it's correct
# place, so it's neccesary to sort
# the sublist to the right and to
# the left of it.
def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

A = [2,8,7,1,3,4,5,6,4]
quicksort(A, 0, len(A)-1)
print(A)
