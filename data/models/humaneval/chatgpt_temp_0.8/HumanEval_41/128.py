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
    # initialize the number of collisions to 0
    collisions = 0
    # loop through each pair of cars from opposite directions
    for i in range(n):
        for j in range(n):
            # if the left-to-right car is ahead of the right-to-left car,
            # then they will never collide, so move on to the next pair
            if i < j:
                continue
            # if the left-to-right car is at the same position as the right-to-left car,
            # then they collide, so increment the number of collisions
            elif i == j:
                collisions += 1
            # if the left-to-right car is behind the right-to-left car,
            # then they will collide at some point, so increment the number of collisions
            else:
                collisions += 1
    # return the total number of collisions
    return collisions
