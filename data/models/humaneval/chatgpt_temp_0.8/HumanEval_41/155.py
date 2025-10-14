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
    for i in range(1, n+1):
        # Each car pair covers a distance of 2i-2 between them
        # We need to check if the left-to-right car collides with the right-to-left car
        if i <= n-i:
            # There are n-i pairs of cars that have not yet crossed paths
            # Each pair has a distance of 2i-2 between them
            # If the distance is equal, then they collide
            if (2*i-2) == (2*(n-i)+2):
                collision_count += 1
        else:
            # If we've checked all possible pairs, we can stop
            break
    return collision_count
