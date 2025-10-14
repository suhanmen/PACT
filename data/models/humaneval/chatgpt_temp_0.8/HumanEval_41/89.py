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
    left_cars = [i for i in range(n)]  # cars moving left to right
    right_cars = [i for i in range(n)]  # cars moving right to left

    collisions = 0
    left_index, right_index = 0, 0

    while left_index < n and right_index < n:
        if left_cars[left_index] < right_cars[right_index]:
            left_index += 1
        elif left_cars[left_index] > right_cars[right_index]:
            right_index += 1
        else:  # collision
            collisions += 1
            left_index += 1
            right_index += 1

    return collisions
