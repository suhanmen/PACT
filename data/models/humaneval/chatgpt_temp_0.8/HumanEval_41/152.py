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
    # Assuming all cars have a constant speed of 1 unit per time step,
    # the time it takes them to meet in the middle is n time steps.
    # Therefore, we only need to count how many pairs of cars will meet
    # during that time.

    # There are n cars moving left to right, and n cars moving right to left.
    # Each car moving left to right will meet exactly one car moving right to left.
    # Therefore, we only need to count how many cars moving right to left
    # will be in the way of cars moving left to right.

    # Each car moving right to left will meet exactly one car moving left to right,
    # but some cars moving right to left will be passed by other cars moving right to left,
    # and therefore will not collide with any cars moving left to right.

    # In order to count the number of collisions, we can assume that each car moving left to right
    # will pass all cars moving right to left that are currently to its left.
    # Therefore, we only need to count the number of cars moving right to left that are to the left
    # of each car moving left to right.

    # We can do this by counting the number of integers k such that 0 <= k < n,
    # and (n-1) - k < k, i.e. k > (n-1) / 2.
    # This condition means that k is to the right of the middle of the road.

    return sum(1 for k in range(n) if k > (n-1) / 2)
