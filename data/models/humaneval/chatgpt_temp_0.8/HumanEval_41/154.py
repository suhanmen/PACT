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
    # Each car has an equal chance of colliding with any other car
    # in the opposite direction.
    # Thus, the probability of a car colliding with another car
    # in the opposite direction is 1 / n.
    # To find the expected value of the number of collisions,
    # we take the sum of all probabilities and multiply by n.
    # This gives us the expected number of collisions.
    probability_of_collision = 1 / n
    expected_number_of_collisions = probability_of_collision * n
    return expected_number_of_collisions
