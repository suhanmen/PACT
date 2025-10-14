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
    # Let's assume that each car moves at a speed of 1 unit per second.
    # We can represent the position of each car by the time it takes to get there.
    # For example, if a car is at position x at time t, it will be at position
    # x + t after t seconds.
    # We can represent the positions of all left-moving cars as a list of integers
    # representing the times it takes them to reach a certain point on the road.
    # We can represent the positions of all right-moving cars as a list of negative
    # integers (since they are moving in the opposite direction).
    # We can then sort both lists in ascending order, since collisions can only happen
    # between cars that are closest to each other.
    # Finally, we can iterate through both lists at the same time, and count the number
    # of collisions that occur.

    left_cars = sorted(range(n))
    right_cars = sorted(range(-n, 0))

    num_collisions = 0
    left_idx = 0
    right_idx = 0
    while left_idx < n and right_idx < n:
        if left_cars[left_idx] < abs(right_cars[right_idx]):
            # The left-moving car is still behind the right-moving car,
            # so there can be no collision.
            left_idx += 1
        elif left_cars[left_idx] > abs(right_cars[right_idx]):
            # The right-moving car is still behind the left-moving car,
            # so there can be no collision.
            right_idx += 1
        else:
            # The two cars are at the same position, so they collide.
            num_collisions += 1
            left_idx += 1
            right_idx += 1

    return num_collisions
