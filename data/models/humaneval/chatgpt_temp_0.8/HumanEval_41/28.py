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
    # The number of cars moving in each direction is equal to n
    # We assume that each car is located at a different position on the road
    # We also assume that all cars are moving at the same speed
    # To find the number of collisions, we need to count the number of pairs of cars that are head-on
    # Since the cars are infinitely sturdy, we can ignore the collision and count it as a collision
    # We can count the number of pairs by multiplying n by (n-1) and then dividing by 2
    return n*(n-1)//2
