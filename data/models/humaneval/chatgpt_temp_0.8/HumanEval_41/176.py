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
    if n <= 0:
        return 0
    
    # We will assume that the cars start at positions (0, 1, 2, ..., n-1) and (2n-1, 2n-2, ..., n).
    # We can do this without loss of generality, since we could always relabel the cars if needed.
    left_cars = list(range(n))
    right_cars = list(range(2*n-1, n-1, -1))
    
    collisions = 0
    idx_left = 0
    idx_right = 0
    
    while idx_left < n and idx_right < n:
        if left_cars[idx_left] < right_cars[idx_right]:
            # The next left car is behind the next right car, so there will be no collision.
            idx_left += 1
        else:
            # The next left car is ahead of the next right car, so there will be a collision with all
            # the left cars up to this one.
            collisions += (n - idx_left)
            idx_right += 1
    
    return collisions
