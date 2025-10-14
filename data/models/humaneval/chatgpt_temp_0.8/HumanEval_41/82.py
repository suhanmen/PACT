# CANNOT PARSE CODE SNIPPET
python
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

    Args:
        n: The number of cars moving in each direction.

    Returns:
        The number of collisions that occur.

    """
    # If there are no cars, there can be no collisions.
    if n == 0:
        return 0

    # Each car is represented as a tuple (position, direction), where
    # direction is -1 for left-to-right cars and 1 for right-to-left cars.
    cars = [(i, -1) for i in range(n)] + [(i, 1) for i in range(n, 2*n)]

    # We sort the cars by their initial position.
    cars.sort()

    # We keep track of the "rightmost" car going in each direction.
    rightmost = {-1: -1, 1: 2*n}

    # We count the number of collisions.
    collisions = 0

    # We iterate over the cars in the order they appear on the road.
    for pos, direction in cars:
        # If this car is going left to right and there is a car going
        # right to left to its right, then they will collide.
        if direction == -1 and rightmost[1] > pos:
            collisions += 1
        # If this car is going right to left and there is a car going
        # left to right to its left, then they will collide.
        if direction == 1 and rightmost[-1] < pos:
            collisions += 1
        # We update the rightmost car going in this direction.
        rightmost[direction] = pos

    return collisions
