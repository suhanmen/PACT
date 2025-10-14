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
    # initialize the position of the cars
    left_to_right = [i for i in range(n)]
    right_to_left = [i for i in range(n, 2*n)]
    
    # initialize the number of collisions to 0
    collisions = 0
    
    # simulate the movement of the cars
    for i in range(n):
        if left_to_right[i] >= right_to_left[-i-1]:
            collisions += 1
    
    return collisions
