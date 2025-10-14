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
    # We can represent each car as a tuple (position, direction), where
    # position is the distance from some fixed point on the road, and direction
    # is either 1 (right to left) or -1 (left to right).
    cars = [(i, -1) for i in range(n)] + [(i, 1) for i in range(n, 2*n)]
    cars.sort()  # Sort the cars by their positions

    # Initialize a counter for the collisions
    collisions = 0

    # Loop over all pairs of cars that are moving towards each other
    for i in range(n):
        j = n + i
        if cars[i][1] == 1 and cars[j][1] == -1:
            if cars[i][0] <= cars[j][0]:
                collisions += 1
            else:
                break  # No more collisions possible

    return collisions
