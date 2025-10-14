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
    # there are n cars going left to right and n cars going right to left
    # assume they start at distance 1000 from each other
    left_cars = [1000 + i*10 for i in range(n)]
    right_cars = [-1000 - i*10 for i in range(n)]
    collisions = 0
    for l_car in left_cars:
        for r_car in right_cars:
            if l_car == -r_car:
                collisions += 1
    return collisions
