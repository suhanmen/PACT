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
    for i in range(n):
        # Calculate the time it will take for the two cars to collide
        time_to_collision = float('inf') if i == 0 else (i / 2)
        # Check if the time is the same for the other cars on the opposite direction
        for j in range(n):
            if i == j:
                continue
            if time_to_collision == float('inf'):
                collision_count += 1
            elif time_to_collision == (n - j) / 2:
                collision_count += 1
    return collision_count
