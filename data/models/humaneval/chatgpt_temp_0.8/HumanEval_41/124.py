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

    :param n: the number of cars in each direction
    :return: the number of collisions
    """
    # We can assume that the left-to-right cars are moving towards positive infinity,
    # and the right-to-left cars are moving towards negative infinity. We can also assume
    # that the cars start at positions 0, 1, 2, ..., n-1 (L-to-R) and -1, -2, -3, ..., -n (R-to-L).
    # Therefore, we can represent each car as a pair (position, direction), where direction is
    # either 1 (for L-to-R) or -1 (for R-to-L).
    # We can create two lists of tuples to represent the cars:
    cars_L_to_R = [(i, 1) for i in range(n)]
    cars_R_to_L = [(-i-1, -1) for i in range(n)]
    # We can then sort the two lists by position, so that we can compare the cars that are closest
    # to each other (in terms of distance to the origin).
    cars_L_to_R.sort()
    cars_R_to_L.sort()
    # We can now iterate over the two lists in parallel, and count the collisions:
    count = 0
    i = 0
    j = 0
    while i < n and j < n:
        if cars_L_to_R[i][0] < cars_R_to_L[j][0]:
            # The next L-to-R car is still behind the next R-to-L car, so no collision yet
            i += 1
        elif cars_L_to_R[i][0] > cars_R_to_L[j][0]:
            # The next R-to-L car is still behind the next L-to-R car, so no collision yet
            j += 1
        else:
            # The next L-to-R car and the next R-to-L car are at the same position, so collision!
            count += 1
            i += 1
            j += 1
    return count
