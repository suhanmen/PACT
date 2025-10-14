Here is the Python function implemented in a markdown style code block:

```python
def wind_chill(velocity, temperature):
    """
    Calculate the wind chill index rounded to the next integer.

    Parameters:
    velocity (float): Wind velocity in km/h.
    temperature (float): Temperature in celsius.

    Returns:
    int: Wind chill index rounded to the next integer.
    """
    wind_chill_index = 13.12 + 0.6215*temperature - 11.37*velocity**0.16 + 0.3965*temperature*velocity**0.16
    return round(wind_chill_index)

# Test the function
assert wind_chill(120,35)==40
```

This function calculates the wind chill index using the formula provided in the problem statement. The result is then rounded to the next integer using the `round()` function. The test case `wind_chill(120,35)==40` is used to verify the function.
