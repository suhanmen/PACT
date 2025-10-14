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
    collision_count = 0
    
    # The nth car from the left will meet the nth car from the right at exactly the same time.
    # Therefore, we only need to check the first n cars from the left and the first n cars from the right.
    for i in range(n):
        # The i-th car from the left will meet the (n-1)-th car from the right.
        # Therefore, we only need to check the first n-i cars from the right.
        for j in range(n-i):
            collision_count += 1
    
    return collision_count
