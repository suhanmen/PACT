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

    # We can represent the positions of the cars as two lists of n integers.
    # The left-to-right cars start at position 0 and move towards the right,
    # while the right-to-left cars start at position n-1 and move towards the left.
    ltr_cars = list(range(n))
    rtl_cars = list(range(n-1, -1, -1))

    # We can iterate over the positions of the cars simultaneously,
    # checking if any of them collide at each time step.
    collisions = 0
    for i in range(n):
        if ltr_cars[i] >= rtl_cars[i]:
            collisions += 1

    return collisions
