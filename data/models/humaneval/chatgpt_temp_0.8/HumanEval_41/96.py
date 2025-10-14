# CANNOT PARSE CODE SNIPPET
python
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
    # We can assume that each car is at a different position along the road
    # and that the left-to-right cars are moving toward higher positions
    # and the right-to-left cars are moving toward lower positions.
    # Therefore, we can represent each car by its position and its direction (+1 or -1).
    cars = [(i, 1) for i in range(n)] + [(i, -1) for i in range(n)]
    cars.sort()  # sort the list by position

    collisions = 0
    for i in range(2 * n):
        for j in range(i + 1, 2 * n):
            if cars[i][1] == 1 and cars[j][1] == -1 and cars[i][0] < cars[j][0]:
                # car i is left-to-right and car j is right-to-left and i is in front of j
                collisions += 1
            else:
                # by the sorting order, there can be no more collisions between cars i and j
                break

    return collisions
