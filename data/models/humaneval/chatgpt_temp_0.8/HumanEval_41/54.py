import random

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
    collision_count = 0
    positions = set()
    for i in range(n):
        left_to_right = random.randint(0, 10000)
        right_to_left = random.randint(0, 10000)
        position = left_to_right - right_to_left
        if position in positions:
            collision_count += 1
        else:
            positions.add(position)
    return collision_count
