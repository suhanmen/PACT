Here is the completed code snippet:

```python
def wind_chill(velocity, temperature):
    wind_chill_index = 13.12 + 0.6215 * temperature - 11.37 * velocity**0.16 + 0.3965 * temperature * velocity**0.16
    return round(wind_chill_index)

assert wind_chill(120, 35) == 40
```

In this code, the `wind_chill` function takes two parameters: `velocity` (wind velocity in km/h) and `temperature` (temperature in celsius). It calculates the wind chill index using the formula provided and rounds the result to the next integer using the `round` function. The calculated wind chill index is then returned.

The `assert` statement at the end of the code verifies that the `wind_chill` function returns the expected result for the given input values.