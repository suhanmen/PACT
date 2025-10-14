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
    left_cars = [i * 2 for i in range(n)]  # positions of left-moving cars
    right_cars = [i * 2 + 1 for i in range(n)]  # positions of right-moving cars
    collisions = 0
    i, j = 0, 0  # indices for left_cars and right_cars
    while i < n and j < n:
        if left_cars[i] < right_cars[j]:
            i += 1  # left car moves ahead
        else:
            collisions += 1  # collision detected
            j += 1  # right car moves ahead
    return collisions
