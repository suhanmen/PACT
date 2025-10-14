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
    # Calculate the distance between each pair of cars
    distance = 2*n
    
    # Calculate the time it takes for the two cars to collide
    time_to_collide = distance / (2*1)
    
    # Calculate the number of collisions that will occur in this time
    num_collisions = n * (n-1) / 2
    
    return int(num_collisions)
