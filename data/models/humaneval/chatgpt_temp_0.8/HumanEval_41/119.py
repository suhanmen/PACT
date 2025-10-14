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
    # Total number of collisions
    collisions = 0
    
    # For each car moving left to right
    for i in range(n):
        # For each car moving right to left
        for j in range(n):
            # Calculate the time it would take for the two cars to collide
            time_to_collision = (j+1)/(2*(i+1))
            
            # If the time is less than or equal to 1, there is a collision
            if time_to_collision <= 1:
                collisions += 1
    
    return collisions
