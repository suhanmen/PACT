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
    # We can represent the positions of the cars using two arrays
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n, 2*n)]

    # We can simulate the movement of the cars by iterating over time steps
    collisions = 0
    for t in range(2*n):
        # At each time step, we check for collisions between the cars
        for i in range(n):
            if left_cars[i] == right_cars[i]:
                collisions += 1
        # We update the positions of the cars by moving them one step forward
        left_cars = [x+1 for x in left_cars]
        right_cars = [x-1 for x in right_cars]

    return collisions
