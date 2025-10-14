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
    # The number of collisions is the same as the number of pairs of cars that pass each other.
    # Each car moving left to right will pass each car moving right to left exactly once.
    # Therefore, the number of pairs of cars that pass each other is equal to the product of
    # the number of cars moving left to right and the number of cars moving right to left.
    return n**2
