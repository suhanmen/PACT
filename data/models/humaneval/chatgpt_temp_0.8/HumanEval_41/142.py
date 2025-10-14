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
    # Since all cars move at the same speed, we only need to consider the relative velocity
    # of the two sets of cars. We can assume that the cars moving left to right have a velocity
    # of +1, and the cars moving right to left have a velocity of -1.
    
    # We can represent each car as a tuple (position, direction), where position is the initial
    # position of the car a
