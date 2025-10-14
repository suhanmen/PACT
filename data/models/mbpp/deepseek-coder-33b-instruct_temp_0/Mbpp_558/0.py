Here is the Python function to find the sum of the per-digit difference between two integers:

```python
def digit_distance_nums(num1, num2):
    # Convert the numbers to strings
    str_num1 = str(num1)
    str_num2 = str(num2)

    # Make both strings the same length by adding leading zeros
    max_len = max(len(str_num1), len(str_num2))
    str_num1 = str_num1.zfill(max_len)
    str_num2 = str_num2.zfill(max_len)

    # Calculate the sum of the per-digit difference
    sum_difference = 0
    for i in range(max_len):
        sum_difference += abs(int(str_num1[i]) - int(str_num2[i]))

    return sum_difference
```

You can test the function with the provided assertion:

```python
assert digit_distance_nums(1,2) == 1
```

This function works by first converting the input numbers to strings. It then makes both strings the same length by adding leading zeros if necessary. After that, it calculates the sum of the per-digit difference by iterating over the digits of the two numbers and adding the absolute difference of the corresponding digits to the sum.
