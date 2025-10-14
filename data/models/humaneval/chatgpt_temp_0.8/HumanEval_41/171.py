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
    # We can imagine this as two lines of cars moving towards each other.
    # Since they are moving at the same speed, we can just compare the relative positions
    # of the cars on each line.
    # We keep track of the position of the rightmost car on the left-moving line
    # and the leftmost car on the right-moving line.
    # If the left-moving car is ahead of the right-moving car, there is no collision.
    # Otherwise, there is a collision and we update the positions of the cars.
    left_pos = 0
    right_pos = float('inf')
    collisions = 0
    while True:
        if left_pos >= right_pos:
            collisions += 1
            right_pos += 1
        else:
            left_pos += 1
        if collisions == n:
            break
    return collisions
