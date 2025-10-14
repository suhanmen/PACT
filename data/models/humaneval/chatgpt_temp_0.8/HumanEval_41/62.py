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
    # In order for a collision to occur, a left-moving car must pass a right-moving car
    # We can imagine the left-moving cars starting at position 0 and the right-moving cars
    # starting at position 2n. Then, if we sort the positions of all 2n cars, we can count
    # the number of pairs of adjacent cars where one is moving left and one is moving right.
    positions = list(range(2*n))
    collisions = 0
    for i in range(1, 2*n):
        if i % 2 == 1:
            # This car is moving left to right
            if positions[i] < positions[i-1]:
                # This car collided with the previous car, which is moving right to left
                collisions += 1
    return collisions
