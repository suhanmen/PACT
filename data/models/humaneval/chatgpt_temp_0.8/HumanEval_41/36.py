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
    # The distance between the two sets of cars is initially very large
    distance_between_cars = 1000000

    # The time it takes for the cars to collide depends on the distance between them
    time_to_collision = distance_between_cars / (2 * n)

    # The number of collisions that occur is equal to the number of left-moving cars times
    # the number of right-moving cars, since each left-moving car can collide with any of
    # the right-moving cars
    num_collisions = n * n

    # We can use the time it takes for the cars to collide to adjust the number of collisions
    # based on the fact that each pair of cars can only collide once
    for i in range(n):
        num_collisions -= (i * 2 + 1) * 2
        num_collisions += 2 * (n - i - 1) * (i + 1)

    return num_collisions
