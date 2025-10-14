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
    # The minimum distance between two cars needed for a collision to occur
    collision_distance = 1

    # The total distance between the frontmost car from the left and the frontmost car from the right
    total_distance = n * 2

    # The distance remaining for the two frontmost cars to collide
    remaining_distance = total_distance - collision_distance

    # The number of collisions that have occurred so far
    num_collisions = 0

    while remaining_distance > 0:
        # Calculate the time it will take for the two frontmost cars to collide
        time_to_collision = remaining_distance / 2

        # Update the remaining distance
        remaining_distance -= time_to_collision * 2

        # Update the number of collisions
        num_collisions += 1

    return num_collisions
