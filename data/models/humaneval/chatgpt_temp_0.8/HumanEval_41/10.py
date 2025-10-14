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
    # We assume that the left-to-right cars are moving from left to right starting at position 0,
    # while the right-to-left cars are moving from right to left starting at position n.
    # We keep track of the positions of the left-to-right cars and the right-to-left cars using two lists.
    ltr_positions = [0]*n
    rtl_positions = [n]*n
    
    # We keep track of the number of collisions so far.
    num_collisions = 0
    
    # We simulate the movement of the cars until they have all passed each other.
    while ltr_positions[-1] < n:
        # We check each pair of left-to-right and right-to-left cars to see if they collide.
        for i in range(n):
            if ltr_positions[i] == rtl_positions[i]:
                num_collisions += 1
        # We update the positions of the cars.
        for i in range(n):
            ltr_positions[i] += 1
            rtl_positions[i] -= 1
    
    return num_collisions
