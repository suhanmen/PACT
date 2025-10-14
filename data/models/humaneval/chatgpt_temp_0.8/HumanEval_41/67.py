# CANNOT PARSE CODE SNIPPET
def car_race_collision(n: int) -> int:
    # The number of collisions is equal to the number of pairs of cars
    # that meet each other while traveling in opposite directions.
    # Since cars move at the same speed, we can assume that they
    # start meeting each other when they are all at the same distance
    # from each other.
    # Thus, the distance between each pair of opposite-direction cars
    # is (n - 1) units.
    # We can consider the left-to-right cars to be fixed at their
    # starting positions, and imagine the right-to-left cars moving
    # towards them. Each time a right-to-left car crosses the position
    # of a left-to-right car, we count that as a collision.
    # Since there are n right-to-left cars, each of which crosses
    # n positions of left-to-right cars, there are n^2 potential collisions.
    # However, we need to exclude the cases where two right-to-left cars
    # pass each other without colliding. This happens when the right-to-left
    # cars are in the order R1R2...Ri...Rj...Rn and Rj crosses the position
    # of Ri before Ri crosses the position of Rj. There are (n choose 2) such
    # pairs of indices (i, j) that we need to exclude.
    
    num_collisions = n**2
    
    for i in range(n):
        for j in range(i+1, n):
            if (n - j) < (j - i):
                # the remaining right-to-left cars have already
                # passed the left-to-right car at position i, so
                # we don't need to check the rest of the cars
                break
            num_collisions -= 1
    
    return num_collisions
