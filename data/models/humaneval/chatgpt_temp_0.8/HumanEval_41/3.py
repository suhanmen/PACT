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
    # We can represent the positions of the left-to-right cars as a list of integers
    # and the positions of the right-to-left cars as a list of negative integers.
    # For example, if n = 3 and the cars are at positions 1, 3, and 5 (from left to right),
    # and positions -2, -4, and -6 (from right to left), we can represent them as:
    # left_cars = [1, 3, 5]
    # right_cars = [-2, -4, -6]
    left_cars = list(range(1, 2*n, 2))
    right_cars = list(range(-2*n+1, 0, 2))

    # We can simulate the movement of the cars by updating their positions at each time step.
    # If a left-to-right car has a higher position than a right-to-left car at any time step,
    # they will collide. We can count the number of collisions by keeping track of the colliding
    # pairs of cars.
    collisions = 0
    for i in range(2*n):
        for j in range(i+1, 2*n):
            if left_cars[i] > right_cars[j]:
                collisions += 1
            else:
                break

    return collisions
