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
    # We can assume that the left-moving cars are at position 0 and the right-moving cars are at position 1
    # We can also assume that the speed of the cars is 1 unit per time step
    # We can represent the positions of the cars using two lists
    left_cars = [0] * n
    right_cars = [1] * n
    
    # We can keep track of the number of collisions using a counter
    num_collisions = 0
    
    # We can simulate the movement of the cars by iterating through time steps
    for t in range(1, 2*n):
        # At each time step, we move the cars one unit to the right or left
        for i in range(n):
            if left_cars[i] < t:
                left_cars[i] += 1
            if right_cars[i] < t:
                right_cars[i] += 1
        
        # We check for collisions by comparing the positions of the left-moving and right-moving cars
        for i in range(n):
            if left_cars[i] == right_cars[i]:
                num_collisions += 1
    
    return num_collisions