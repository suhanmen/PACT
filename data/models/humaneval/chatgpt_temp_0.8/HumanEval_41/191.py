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
    # We can model the positions of the cars as two parallel lines moving towards each other.
    # If we represent the position of each car on each line as a number, we can compare them
    # to see if any cars are colliding.
    
    # Initialize the positions of the left-to-right cars and the right-to-left cars.
    ltr_positions = list(range(n))
    rtl_positions = list(range(n, 2*n))
    
    # Initialize the number of collisions to 0.
    num_collisions = 0
    
    # As long as there are still cars on both sides, keep checking for collisions.
    while ltr_positions and rtl_positions:
        # Get the positions of the first car on each side.
        ltr_pos = ltr_positions[0]
        rtl_pos = rtl_positions[0]
        
        # If they collide, remove them from the lists and increment the collision counter.
        if ltr_pos == rtl_pos:
            ltr_positions.pop(0)
            rtl_positions.pop(0)
            num_collisions += 1
        # Otherwise, move the car that's f
