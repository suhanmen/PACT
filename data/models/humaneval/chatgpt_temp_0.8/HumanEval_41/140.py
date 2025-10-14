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
    # There will be n * n possible collisions since each left to right car can collide with each right to left car
    # Initialize a counter to keep track of the number of collisions
    num_collisions = 0
    
    # Loop through each left to right car
    for i in range(n):
        # Loop through each right to left car
        for j in range(n):
            # If the distance between the two cars is an even number (meaning they will collide), increment the counter
            if (i + j) % 2 == 0:
                num_collisions += 1
    
    return num_collisions
