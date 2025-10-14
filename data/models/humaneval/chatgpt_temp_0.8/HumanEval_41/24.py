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
    # There can be at most n collisions
    collisions = 0
    
    # We can think of the cars driving towards each other on the infinite road as
    # two sets of points moving towards each other on an infinite line.
    #
    # Let's represent the left-driving cars as a set of n points all at position 0.
    # Let's represent the right-driving cars as a set of n points all at position n.
    #
    # Each point moves at the same speed, so we can represent its motion as adding
    # 1 to its position each time step.
    #
    # At each time step, we check if there are any points that are in the same position.
    # If there are, that means a collision has occurred.
    #
    # We repeat this process until all the left-driving cars have passed all the
    # right-driving cars.
    left_cars = set(range(n))
    right_cars = set(range(n, 2*n))
    while left_cars and right_cars:
        # Move all cars one step
        left_cars = {p + 1 for p in left_cars}
        right_cars = {p - 1 fo
