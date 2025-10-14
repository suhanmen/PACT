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
    # Each car can be identified by its position on the road,
    # which we can represent as a tuple (position, direction),
    # where direction is either 1 (left to right) or -1 (right to left).
    # We'll start by initializing the two sets of cars.
    left_cars = {(i, 1) for i in range(n)}
    right_cars = {(i, -1) for i in range(n)}

    # We'll keep track of the number of collisions we encounter.
    collisions = 0

    # We'll simulate the movement of the cars by iterating over time steps.
    # At each time step, each car moves one unit in its direction.
    # We'll stop when there are no more left-moving cars or right-moving cars left.
    while left_cars and right_cars:
        # First, we'll update the position of each car.
        left_cars = {(pos+1, dir) for (pos, dir) in left_cars}
        right_cars = {(pos-1, dir) for (pos, dir) in right_cars}

        # Next, we'll check for collisions. A collision occurs when a left-moving car
        # and a right-moving car have the same position. We'll count each collision and
        # remove the collided cars from their respective sets.
        collisions += len(left_cars & right_cars)
        left_cars -= left_cars & right_cars
        right_cars -= left_cars & right_cars

    return collisions
