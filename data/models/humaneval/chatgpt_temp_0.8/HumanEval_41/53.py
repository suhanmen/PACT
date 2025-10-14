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
    # We can think of each left-to-right car as a point moving to the right,
    # and each right-to-left car as a point moving to the left.
    # The goal is to count how many pairs of points intersect.
    # This is equivalent to counting how many times a point to the right
    # of the midpoint between two points to the left, passes that midpoint.

    # First, let's create a list of positions for the left-to-right cars.
    # We can assume they start at the origin and move to the right.
    ltr_positions = list(range(n))

    # Then, let's create a list of positions for the right-to-left cars.
    # We can assume they start at the end of the road and move to the left.
    rtl_positions = list(range(n, 2 * n))

    # We can now count how many times a point to the right of a midpoint
    # passes that midpoint, for all midpoints.

    # To do this, we can iterate over all pairs of left-to-right and right-to-left
    # positions, and count how many of them have a right-to-left car to the left of
    # a left-to-right car.

    count = 0
    for i in range(n):
        for j in range(n):
            if (ltr_positions[i] < rtl_positions[j]) and (ltr_positions[i+1] > rtl_positions[j+1]):
                count += 1

    return count
