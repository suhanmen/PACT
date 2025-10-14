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
    # We can assume the left to right cars are starting from position 0
    # and the right to left cars are starting from position (n+1)*100 (arbitrary large number)
    collisions = 0
    for i in range(n):
        # The distance between the two cars when they pass each other is (n-i)*100
        # Since they're moving at the same speed, the time it takes for them to collide is (n-i)*100/100, or n-i
        # We only need to check for collisions up to the nth car, since the remaining cars will have already passed each other
        if i < n-1:
            collisions += n-i-1
    return collisions
