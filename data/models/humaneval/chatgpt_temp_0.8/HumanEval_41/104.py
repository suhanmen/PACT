python
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
    # we'll solve this problem by counting the number of cars moving left to right that will collide
    # with a car moving right to left. since all cars move at the same speed, we can assume that each
    # car moving left to right will eventually pass all cars moving right to left, so we only need to
    # consider the relative positions of the cars at the beginning
    
    # let
