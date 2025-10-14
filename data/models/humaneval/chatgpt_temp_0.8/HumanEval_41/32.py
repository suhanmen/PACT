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
    # we assume each car moves at a speed of 1 unit per second
    # we also assume that the cars are placed randomly on the road
    # so we can sort the positions of the cars to simplify the counting process
    left_to_right_cars = sorted([random.uniform(0, 100) for i in range(n)])
    right_to_left_cars = sorted([random.uniform(0, 100) for i in range(n)], reverse=True)
    collisions = 0
    i = j = 0
    while i < n and j < n:
        if left_to_right_cars[i] > right_to_left_cars[j]:
            # a collision occurred
            collisions += 1
            j += 1
        else:
            i += 1
    return collisions
