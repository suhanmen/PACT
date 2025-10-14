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
    # direction is -1 for left-to-right cars and +1 for right-to-left cars.
    cars = [(i, -1) for i in range(n)] + [(i, 1) for i in range(n, 2*n)]
    cars.sort()  # Sort by position

    collisions = 0
    for i in range(2*n):
        for j in range(i+1, 2*n):
            if cars[i][1] == -1 and cars[j][1] == 1:  # They're moving towards each other
                if cars[i][0] < cars[j][0]:  # They collide
                    collisions += 1
                else:  # All subsequent pairs will also not collide
                    break

    return collisions
