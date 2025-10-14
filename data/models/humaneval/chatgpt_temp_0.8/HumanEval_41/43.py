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
    # Each car is represented by a tuple with two elements:
    # its starting position and its direction (1 for left to right, -1 for right to left)
    cars = [(i, 1) for i in range(n)] + [(i, -1) for i in range(n, 2 * n)]
    # Sort the cars by their starting position
    cars.sort()
    # Keep track of the number of collisions
    collisions = 0
    # Iterate over all pairs of cars that could collide
    for i in range(len(cars) - 1):
        if cars[i][1] == 1 and cars[i+1][1] == -1:
            # If the current car is going left to right and the next car is going right to left,
            # they will collide if the current car's position is less than the next car's position
            if cars[i][0] < cars[i+1][0]:
                collisions += 1
    return collisions
