def car_race_collision(n: int):
    total_collisions = 0
    for i in range(n):
        # calculate position of left-to-right car i at time t
        pos_i = i + 1
        
        for j in range(n):
            # calculate position of right-to-left car j at time t
            pos_j = -j - 1
            
            # check if cars i and j collide at time t
            if pos_i == abs(pos_j):
                total_collisions += 1
    
    return total_collisions
