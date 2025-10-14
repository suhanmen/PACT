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
    # We can assume that the left to right cars start at position 0 and the right to left
    # cars start at position n+1 (assuming 1-indexing).
    ltr_cars = set(range(n))
    rtl_cars = set(range(n+1, 2*n+1))
    collisions = 0
    
    # We simulate the movement of the cars by incrementing their position by 1 in each step.
    # We stop when there are no more cars on the road.
    while ltr_cars and rtl_cars:
        # We find the positions of the leftmost ltr car and the rightmost rtl car.
        ltr_pos = min(ltr_cars)
        rtl_pos = max(rtl_cars)
        
        # If the ltr car is behind the rtl car, no more collisions are possible.
        if ltr_pos >= rtl_pos:
            break
        
        # Otherwise, we remove the collided cars from their sets and record the collision.
        ltr_cars.discard(ltr_pos)
        rtl_cars.discard(rtl_pos)
        collisions += 1
        
    return collisions
