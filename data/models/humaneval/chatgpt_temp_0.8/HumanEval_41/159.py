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
    # Since all cars move at same speed, we can just consider the distance between them
    # and calculate the time it takes for them to collide
    # Once we know the time, we can check if it is an integer value or not to determine if
    # there is a collision or not

    # distance between two cars at start
    distance = 10**9

    # relative speed of two cars
    relative_speed = 200

    # time taken for collision
    time = distance/relative_speed

    # number of collisions
    collisions = n * (n-1) // 2

    return collisions
