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
    speed = 1  # All cars move at the same speed
    distance_between_cars = 1  # The distance between cars is 1 unit of distance
    time_to_collide = distance_between_cars / speed
    total_time = 2 * n * time_to_collide
    total_collisions = n * n
    return total_collisions
