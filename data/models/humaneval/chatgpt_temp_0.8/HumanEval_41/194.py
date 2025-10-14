# CANNOT PARSE CODE SNIPPET
def car_race_collision(n: int) -> int:
    # We can represent each car as a pair (position, direction),
    # where direction is either -1 (left to right) or 1 (right to left).
    cars = [(i, -1) for i in range(n)] + [(i, 1) for i in range(n, 2*n)]

    # Sort the cars by position, breaking ties by direction (right to left first).
    cars.sort(key=lambda c: (c[0], -c[1]))

    # Count the number of collisions.
    collisions = 0
    for i in range(1, 2*n):
        if cars[i][1] == -1 and cars[i-1][1] == 1:
            collisions += 1

    return collisions
