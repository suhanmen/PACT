# CANNOT PARSE CODE SNIPPET
def car_race_collision(n: int) -> int:
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """
    # We can imagine the cars as points moving in opposite directions
    # on a line, and count the number of times they cross each other.
    # This is the same as counting the number of inversions in a list
    # of n elements, where the i-th element represents the position of
    # the i-th car moving left to right.
    positions = list(range(n))
    return count_inversions(positions)

def count_inversions(arr: List[int]) -> int:
    """
    Counts the number of inversions in a list of integers using
    a modified merge-sort algorithm.
    """
    if len(arr) <= 1:
        return 0
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    count = count_inversions(left) + count_inversions(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            count += len(left) - i
        k += 1
    arr[k:] = left[i:] + right[j:]
    return count
