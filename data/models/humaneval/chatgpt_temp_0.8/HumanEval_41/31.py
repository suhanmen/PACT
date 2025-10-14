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
    # We'll keep track of the positions of the cars in two lists:
    # one for the left-to-right cars, and one for the right-to-left cars.
    # We'll initialize them to be very far away from each other, so that
    # there are no collisions at the start.
    ltr_cars = [i * 1000000 for i in range(n)]
    rtl_cars = [i * 1000000 for i in range(n)]
    
    # We'll also keep track of the number of collisions we've seen so far.
    num_collisions = 0
    
    # We'll simulate the movement of the cars over time.
    # Each iteration of this loop represents one "time step".
    for i in range(1000000):
        # We'll check if any of the left-to-right cars have collided with
        # any of the right-to-left cars at this time step.
        for j in range(n):
            if ltr_cars[j] == rtl_cars[j]:
                num_collisions += 1
        
        # We'll update the positions of the cars for the next time step.
        # All the cars are moving at the same speed, so we just add 1 to
        # the positions of the left-to-right cars and subtract 1 from the
        # positions of the right-to-left cars.
        ltr_cars = [pos + 1 for pos in ltr_cars]
        rtl_cars = [pos - 1 for pos in rtl_cars]
    
    # Once we've simulated all the time steps, we return the final number
    # of collisions we observed.
    return num_collisions
