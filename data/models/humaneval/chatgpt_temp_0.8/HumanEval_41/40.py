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
    # We can represent each car as a pair of integers (position, direction).
    # Direction can be 1 for left-to-right cars and -1 for right-to-left cars.
    # We can assume that all cars are initially sorted by position and that there are no two
    # cars at the same position.
    cars = [(i, 1) for i in range(n)] + [(i, -1) for i in range(n)]
    cars.sort()  # sort the cars by position

    # Count the number of collisions by scanning the cars from left to right.
    collisions = 0
    for i in range(len(cars) - 1):
        if cars[i][1] == 1 and cars[i+1][1] == -1:
            collisions += 1

    return collisions
