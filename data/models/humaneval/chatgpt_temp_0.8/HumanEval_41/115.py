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
    # initialize counter for collisions
    collisions = 0
    
    # simulate the cars' movements
    for i in range(n):
        # calculate the time it takes for the two cars to meet
        time = (2 * i + 1) / (2 * n)
        
        # check if the meeting time is an integer multiple of the speed
        if time % 1 == 0:
            collisions += 1
    
    return collisions
