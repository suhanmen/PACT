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
    # Each car can be denoted by its position on the road.
    # We will represent left-moving cars as positive numbers and
    # right-moving cars as negative numbers.
    # For example, the leftmost left-moving car would be at position n,
    # and the leftmost right-moving car would be at position -n.
    left_cars = list(range(n, 2*n))
    right_cars = list(range(-n, 0))

    # We will keep track of the number of collisions so far.
    collisions = 0

    # We will simulate the movement of the cars for a fixed period of time.
    # Let's say that each time step is 1 second.
    # After 2n seconds, we will stop.
    for t in range(2*n):
        # We will simulate the movement of the left-moving cars.
        # They move 1 unit to the right each second.
        left_cars = [car + 1 for car in left_cars]

        # We will simulate the movement of the right-moving cars.
        # They move 1 unit to the left each second.
        right_cars = [car - 1 for car in right_cars]

        #
