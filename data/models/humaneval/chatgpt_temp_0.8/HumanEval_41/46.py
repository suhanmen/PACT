# CANNOT PARSE CODE SNIPPET
python
def car_race_collision(n: int) -> int:
    # We can simulate the car race by representing each car as a pair
    # (position, direction), where direction is -1 for left-to-right cars
    # and 1 for right-to-left cars.
    cars = [(i * 1000, -1) for i in range(n)] + [(i * 1000, 1) for i in range(n)]

    # We can sort the cars by their position, so that we can check for collisions
    # efficiently as we iterate through the list.
    cars.sort()

    # We can keep track of the number of collisions we encounter.
    collisions = 0

    # We can iterate through the cars and check for collisions.
    for i in range(len(cars) - 1):
        if cars[i][1] == -1 and cars[i+1][1] == 1:
            # If the current car is moving left to right and the next car is moving
            # right to left, they will collide at some point.
            collisions += 1

    return collisions
