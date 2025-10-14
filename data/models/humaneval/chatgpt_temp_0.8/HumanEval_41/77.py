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

    :param n: the number of cars driving in each direction
    :return: the number of collisions that occur
    """
    # We can think of the left-to-right cars as starting at position 0 and moving towards infinity,
    # while the right-to-left cars start at infinity and move towards position 0. We can represent
    # their positions as pairs of integers (pos, dir) where pos is their current position and dir is
    # either -1 or 1 indicating the direction of movement (left or right).
    #
    # We start by initializing two lists, one for the left-to-right cars and one for the right-to-left
    # cars. Each list has n pairs representing the initial positions of the cars.
    left_cars = [(0, 1) for _ in range(n)]
    right_cars = [(float('inf'), -1) for _ in range(n)]
    
    # We keep track of the number of collisions so far.
    num_collisions = 0
    
    # We simulate the movement of the cars until there are no more collisions possible.
    while True:
        # We compute the closest distance between any pair of left-to-right and right-to-left cars.
        closest_distance = min(right_pos - left_pos for (left_pos, _), (right_pos, _) in zip(left_cars, right_cars))
        
        # If the closest distance is positive (i.e., there are still some cars that haven't collided yet),
        # we move all the cars by that distance and check if any collisions occurred.
        if closest_distance > 0:
            for i in range(n):
                left_cars[i] = (left_cars[i][0] + left_cars[i][1] * closest_distance, left_cars[i][1])
                right_cars[i] = (right_cars[i][0] + right_cars[i][1] * closest_distance, right_cars[i][1])
                if left_cars[i][0] >= right_cars[i][0] and left_cars[i][1] > 0 and right_cars[i][1] < 0:
                    num_collisions += 1
        # If the closest distance is non-positive (i.e., all pairs of cars have collided), we stop the simulation.
        else:
            break
    
    return num_collisions
