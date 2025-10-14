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
    collisions = 0
    for i in range(n):
        # calculate the time it takes for the ith car from the left to reach the origin
        time = i + 1
        # calculate the position of the ith car from the right at that time
        position = (n - i) * time
        # if the position of the car from the right is less than or equal to the origin, there is a collision
        if position <= 0:
            collisions += 1
    return collisions
