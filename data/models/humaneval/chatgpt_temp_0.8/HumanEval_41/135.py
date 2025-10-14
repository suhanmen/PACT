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
    # There are n cars moving left to right and n cars moving right to left.
    # We can represent their positions on the road as two sorted lists of integers.
    ltr_cars = [i for i in range(n)]
    rtl_cars = [i for i in range(n, 2*n)]
    
    # We will keep track of the number of collisions.
    collisions = 0
    
    # We will loop through each pair of cars and check if they collide.
    for i in range(n):
        for j in range(n):
            if ltr_cars[i] > rtl_cars[j]:
                # If a car moving left to right is ahead of a car moving right to left,
                # then they will collide and we increase the collision count.
                collisions += 1
    
    return collisions
