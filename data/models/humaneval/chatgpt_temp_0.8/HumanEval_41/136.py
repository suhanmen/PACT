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
    # We can think of each pair of cars as a "collision zone"
    # where a collision can occur if and only if the left car is
    # behind the right car (i.e. the left car's position is less
    # than the right car's position).
    # There are n * n collision zones, since there are n cars going
    # left and n cars going right.
    #
    # To count the number of collisions, we can iterate through all
    # possible collision zones and check if a collision occurs.
    # If it does, we increment a counter and move on to the next
    # collision zone.
    #
    # We can calculate the positions of the cars using their speed
    # and the time elapsed. For example, if all cars are moving at
    # a speed of 1 unit per second, and we want to know their position
    # after 5 seconds, we simply multiply their speed by the time
    # elapsed: position = speed * time.
    #
    # Note that we can assume the time elapsed is the same for all
    # collision zones, since all cars are moving at
