# CANNOT PARSE CODE SNIPPET
python
def car_race_collision(n: int) -> int:
    left_to_right = [False] * n  # list of n cars moving left to right
    right_to_left = [False] * n  # list of n cars moving right to left
    collisions = 0  # number of collisions so far

    while True:
        # update positions of cars moving left to right
        for i in range(n):
            if left_to_right[i]:
                left_to_right[i] = False
                if i < n - 1:
                    left_to_right[i+1] = True

        # update positions of cars moving right to left
        for i in range(n):
            if right_to_left[i]:
                right_to_left[i] = False
                if i < n - 1:
                    right_to_left[i+1] = True

        # check for collisions
        if left_to_right[0] and right_to_left[0]:
            collisions += 1

        # check if all cars have passed each other
        if not any(left_to_right) and not any(right_to_left):
            break

    return collisions
