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

    # calculate the number of collisions
    # each left-moving car will collide with the right-moving car that is closest to it
    # this means that the first left-moving car will collide with the last right-moving car,
    # the second left-moving car will collide with the second-to-last right-moving car, and so on
    # the position of the left-moving car can be represented as n-i, where i is the index of the car
    # the position of the right-moving car can be represented as i
    # the collision will happen when n-i == i, or when i == n/2
    collisions = n // 2

    # return the number of collisions
    return collisions
