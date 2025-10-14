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
    # Let's assume that the cars start at positions 0, 1, 2, ..., n-1 on both sides.
    # The speed of each car is also 1 (in whatever units we are using).
    left_cars = list(range(n))
    right_cars = list(range(n))

    # Let's keep track of the number of collisions.
    num_collisions = 0

    # We will simulate the movement of the cars until they all pass each other.
    while len(left_cars) > 0 and len(right_cars) > 0:
        # The first car on the left side and the first car on the right side are going to
        # meet if and only if the position of the right car is the same as the position
        # of the left car plus n (since they are moving towards each other).
        if right_cars[0] == left_cars[0] + n:
            num_collisions += 1
            # The first car on the left side and the first car on the right side have now
            # collided. We remove them from the lists, since they will not collide with
            # any other car in the future.
            left_cars.pop(0)
            right_cars.pop(0)
        else:
            # If the two cars are not going to collide, then we move the right car one
            # position to the left (i.e., we subtract 1 from its position).
            right_cars[0] -= 1

            # If the position of the right car is now less than the position of the leftmost
            # car on the left side, then the right car has passed all the left cars and we
            # can remove it from the list.
            if right_cars[0] < left_cars[0]:
                right_cars.pop(0)

            # We do the same thing for the left cars, but in the opposite direction.
            left_cars[0] += 1
            if left_cars[0] > right_cars[0]:
                left_cars.pop(0)

    return num_collisions
