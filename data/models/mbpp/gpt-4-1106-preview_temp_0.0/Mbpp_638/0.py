"""
Write a function to calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
assert wind_chill(120,35)==40
"""


import math

def wind_chill(velocity, temperature):
    # Wind chill index formula for km/h and Celsius
    if temperature > 10 or velocity < 4.8:
        return None
    wci = 13.12 + 0.6215 * temperature - 11.37 * math.pow(velocity, 0.16) + 0.3965 * temperature * math.pow(velocity, 0.16)
    return math.ceil(wci)

# Example usage
# assert wind_chill(120, 35) == 40
