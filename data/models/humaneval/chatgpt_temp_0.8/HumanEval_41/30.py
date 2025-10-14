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
    # We can represent the cars moving left to right using a list of numbers
    # indicating their starting positions on the road.
    left_cars = list(range(n))

    # Similarly, we can represent the cars moving right to left using a list of numbers
    # indicating their starting positions on the road, but we need to add the length
    # of the road to each position so that they are moving towards the left.
    right_cars = [i + n for i in range(n)]

    # We can count the number of collisions by counting the number of pairs
    # of cars that are moving towards each other and have a distance of 0 between them.
    num_collisions = 0
    for pos in left_cars:
        if pos in right_cars:
            num_collisions += 1

    return num_collisions
