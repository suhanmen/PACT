# CANNOT PARSE CODE SNIPPET
def car_race_collision(n: int) -> int:
    # Each car is represented as a tuple (position, direction)
    # where direction is 1 for left-to-right cars and -1 for right-to-left cars
    cars = [(0, 1)] * n + [(10 ** 9, -1)] * n  # initial positions
    cars.sort()  # sort by position

    collisions = 0
    for i in range(n):
        if cars[i][1] == 1:  # left-to-right car
            j = i + 1  # start searching from the next car
            while j < 2 * n and cars[j][1] == -1:
                if cars[j][0] < cars[i][0]:
                    collisions += 1
                else:
                    break  # no more possible collisions
                j += 1
        else:  # right-to-left car
            j = i - 1  # start searching from the previous car
            while j >= 0 and cars[j][1] == 1:
                if cars[i][0] > cars[j][0]:
                    collisions += 1
                else:
                    break  # no more possible collisions
                j -= 1

    return collisions
