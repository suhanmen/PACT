"""
Write a function to calculate a dog's age in dog's years.
assert dog_age(12)==61
"""



def dog_age(human_years):
    # Assuming the first two human years equal 10.5 dog years each
    dog_years = 0
    if human_years <= 2:
        dog_years = human_years * 10.5
    else:
        # First two years
        dog_years = 2 * 10.5
        # Remaining years
        dog_years += (human_years - 2) * 4
    return int(dog_years)

# Test case
assert dog_age(12) == 61
