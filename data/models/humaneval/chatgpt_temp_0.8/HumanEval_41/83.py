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
    # we can imagine the two sets of cars as two parallel lines moving towards each other
    # with the same speed. the distance between the two lines will decrease until
    # they finally collide.
    # since all cars have the same speed, the time it takes to collide is equal
    # to the distance between the two lines divided by twice the speed of a car.
    # note that we need to handle the case where there are an odd number of cars,
    # in which case one car will pass through without colliding with another.
    time_to_collide = n // 2 if n % 2 == 0 else (n // 2) + 1
    return time_to_collide
