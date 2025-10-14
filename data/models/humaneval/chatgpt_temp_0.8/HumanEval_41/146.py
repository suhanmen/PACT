# CANNOT PARSE CODE SNIPPET
def car_race_collision(n: int) -> int:
    # Each car is represented by its position on the road.
    # We use sets to keep track of the positions of cars going in
    # opposite directions.
    left_cars = set(range(n))
    right_cars = set(range(n, 2*n))

    # We count the number of collisions seen so far.
    collisions = 0

    # We keep iterating until no more collisions can happen.
    while left_cars and right_cars:
        # We find the leftmost car going left to right and the
        # rightmost car going right to left. If their positions
        # are such that they collide, we count a collision and
        # remove them from their respective sets.
        leftmost = min(left_cars)
        rightmost = max(right_cars)
        if leftmost > rightmost:
            break
        collisions += 1
        left_cars.remove(leftmost)
        right_cars.remove(rightmost)

    return collisions
