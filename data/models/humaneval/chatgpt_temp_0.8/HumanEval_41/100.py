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
    positions = [0] * n * 2
    directions = [1] * n + [-1] * n
    collisions = 0
    
    for i in range(n * 2):
        for j in range(i + 1, n * 2):
            if directions[i] == 1 and directions[j] == -1 and positions[i] < positions[j]:
                collisions += 1
            positions[i] += directions[i]
            positions[j] += directions[j]
    
    return collisions
