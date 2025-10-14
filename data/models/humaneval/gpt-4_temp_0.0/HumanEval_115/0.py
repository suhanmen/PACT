def max_fill(grid, capacity):
    import math

    def count_water_units(grid):
        count = 0
        for row in grid:
            count += row.count(1)
        return count

    water_units = count_water_units(grid)
    bucket_count = math.ceil(water_units / capacity)

    return bucket_count
