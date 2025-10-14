# CANNOT PARSE CODE SNIPPET
def car_race_collision(n: int) -> int:
    # initialize positions and velocities of cars moving left to right and right to left
    left_cars = [(i, 1) for i in range(n)]
    right_cars = [(i, -1) for i in range(n)]
    # initialize collision counter
    collisions = 0
    # iterate through each car moving left to right
    for left_car in left_cars:
        # iterate through each car moving right to left
        for right_car in right_cars:
            # if the left car is at a position greater than or equal to the right car,
            # they will collide
            if left_car[0] >= right_car[0]:
                collisions += 1
        # update the position of the left car
        left_car = (left_car[0] + left_car[1], left_car[1])
    # return the total number of collisions
    return collisions
