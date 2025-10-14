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
    # let the left to right cars be at positions 1, 2, ..., n
    # let the right to left cars be at positions -1, -2, ..., -n
    # initialize two pointers, i and j, to track the position of the cars
    i = 1
    j = -1
    # initialize the collision count to zero
    collision_count = 0
    # loop until i and j meet or pass each other
    while i >= j:
        # if i and j are at the same position, a collision has occurred
        if i == j:
            collision_count += 1
        # move i and j one position to the right and left, respectively
        i += 1
        j -= 1
    # return the collision count
    return collision_count
