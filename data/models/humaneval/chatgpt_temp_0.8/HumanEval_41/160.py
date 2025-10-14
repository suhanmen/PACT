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
    # The left-moving cars will collide with the right-moving ones
    # if and only if they start before them on the road, so we can
    # count the number of collisions by counting the number of pairs
    # of left-moving and right-moving cars where the left-moving one
    # starts before the right-moving one.
    # There are n left-moving cars and n right-moving cars, so there
    # are n^2 possible pairs, but we only need to consider those where
    # the left-moving car starts before the right-moving one.
    count = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                count += 1
    return count
