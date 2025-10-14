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
    # Initialize the collisions counter
    collisions = 0
    
    # Loop through all pairs of cars
    for i in range(n):
        for j in range(n):
            # If a car moving left to right is to the right of a car moving right to left,
            # and they have not already collided, count it as a collision
            if i > j and i + j > n:
                collisions += 1
                
    return collisions
