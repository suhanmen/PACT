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
    # Each car is identified by its speed and starting position
    # For cars going left to right, speed is positive, and position is non-negative
    # For cars going right to left, speed is negative, and position is non-positive
    cars = [(1, i) for i in range(n)] + [(-1, -i) for i in range(n)]
    # Sort the cars by their starting position
    cars.sort(key=lambda x: x[1])
    # Count the number of collisions
    collisions = 0
    for i in range(1, 2*n):
        if cars[i][0] > 0 and cars[i-1][0] < 0:
            collisions += 1
    return collisions
