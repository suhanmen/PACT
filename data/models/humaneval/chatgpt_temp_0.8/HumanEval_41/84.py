# CANNOT PARSE CODE SNIPPET
def car_race_collision(n: int) -> int:
    # we can ignore the actual positions of the cars, as they are irrelevant
    # instead, we just need to keep track of how many left-to-right cars are
    # ahead of each right-to-left car, and vice versa
    ltr_ahead = [0] * n  # number of ltr cars ahead of each rtl car
    rtl_ahead = [0] * n  # number of rtl cars ahead of each ltr car
    for i in range(n):
        # for each ltr car, count how many rtl cars are ahead of it
        for j in range(i+1, n):
            rtl_ahead[i] += 1
        # for each rtl car, count how many ltr cars are ahead of it
        for j in range(i+1, n):
            ltr_ahead[i] += 1
    # now count how many collisions there are by checking pairs of cars
    collisions = 0
    for i in range(n):
        for j in range(n):
            if ltr_ahead[j] >= i+1 and rtl_ahead[i] >= j+1:
                collisions += 1
    return collisions
