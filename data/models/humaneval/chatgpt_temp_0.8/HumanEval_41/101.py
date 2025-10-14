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
    # The left-to-right cars are moving in the positive direction
    # The right-to-left cars are moving in the negative direction
    # We can represent their positions on the number line as two arrays
    pos_ltr = []
    pos_rtl = []
    for i in range(n):
        pos_ltr.append(i)
        pos_rtl.append(-(i+1))
    
    # To count the number of collisions, we can compare the positions
    # of each pair of cars at each time step
    count = 0
    for t in range(1, n):
        for i in range(n):
            if pos_ltr[i] >= pos_rtl[i]:
                count += 1
        # Update the positions of the cars
        for i in range(n):
            pos_ltr[i] += 1
            pos_rtl[i] -= 1
    
    return count
