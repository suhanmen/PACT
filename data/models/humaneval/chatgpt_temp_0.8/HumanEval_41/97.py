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
    # We can assume that the left-moving cars are at position 0 and the right-moving cars are at position 1
    # Each car can be represented as a tuple (position, direction)
    # where direction is 0 for left-moving and 1 for right-moving
    cars = [(0, 0) for _ in range(n)] + [(1, 1) for _ in range(n)]
    cars.sort() # sort by position

    collisions = 0
    for i in range(len(cars)-1):
        if cars[i][1] == 0 and cars[i+1][1] == 1: # a left-moving car hits a right-moving car
            collisions += 1

    return collisions
