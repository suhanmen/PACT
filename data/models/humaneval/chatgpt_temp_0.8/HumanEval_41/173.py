def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right; simultaneously, a different set of n cars
    are driving right to left. The two sets of cars start out being very far from
    each other. All cars move in the same speed. Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """
    # Number of possible collision points is 2n - 1
    # Each collision point can be occupied by at most one car from each direction
    # Therefore, number of collisions is min(n, 2n - 1 - n) = min(n - 1, n)
    return min(n - 1, n)
