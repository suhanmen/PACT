def car_race_collision(n: int):
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
    # We assume that the cars move at a speed of 1 unit per time step
    # We also assume that the distance between two cars moving in opposite directions is 2 units
    # If two cars are at distance d apart, they will collide in d/2 time steps
    # So, if we create a list of distances between opposite-moving cars, we can count the number of collisions
    distances = [2 * (i + 1) for i in range(n)]
    collisions = sum([1 for d in distances if d <= 2 * n])
    return collisions
