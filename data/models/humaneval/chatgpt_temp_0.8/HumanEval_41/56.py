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
    # We can compute the number of collisions by counting the number of pairs of
    # cars that pass each other. Each left-moving car will pass each right-moving car
    # at some point, so there will be n^2 total passes. However, since each car can only
    # collide once (they continue moving after a collision), we need to divide by 2.
    return n * n // 2
